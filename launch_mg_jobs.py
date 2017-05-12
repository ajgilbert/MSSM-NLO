from UserCode.ICHiggsTauTau.jobs import Jobs
import argparse
import os
import ROOT
import json
import subprocess
from math import ceil
from array import array
from itertools import product

job_mgr = Jobs()
parser = argparse.ArgumentParser()

parser.add_argument('--mg-dir', default='./MG5_aMC_v2_3_0_beta')
parser.add_argument('--base', default='./bbH_4FS_yb2')
parser.add_argument('-n', '--nevents', default=500000, type=int)
parser.add_argument('--mg-split', default=10000, type=int)
parser.add_argument('--cores', default=8, type=int)
parser.add_argument('--split', default=-1, type=int)
parser.add_argument('-m', '--mass', default='500')
parser.add_argument('--step', default='none', choices=['none', 'lhe', 'clean', 'gen', 'ntuple', 'xsec'])
parser.add_argument('--upload', default=None)
parser.add_argument('--download', default=None)
parser.add_argument('--usetmp', action='store_true')

job_mgr.attach_job_args(parser)
args = parser.parse_args()
job_mgr.set_args(args)

if args.split == -1:
    args.split = args.nevents


for MASS in args.mass.split(','):
    base_name = os.path.basename(os.path.normpath(args.base))
    workdir = os.path.join(args.mg_dir, '%s_%s' % (base_name, MASS))
    
    if args.step in ['lhe']:
        if os.path.isdir(workdir):
            print 'Dir %s already exists, skipping' % workdir
            continue
        else:
            os.system('cp -r %s %s' % (args.base, workdir))

        with open('%s/Cards/param_card.dat' % (workdir)) as param_file:
            param_cfg = param_file.read()
        param_cfg = param_cfg.replace('{MASS}', '%.5e' % float(MASS))
        with open('%s/Cards/param_card.dat' % (workdir), "w") as outfile:
            outfile.write(param_cfg)
        
        with open('%s/Cards/run_card.dat' % (workdir)) as run_file:
            run_cfg = run_file.read()
        run_cfg = run_cfg.replace('{TOTAL_EVENTS}', '%i' % args.nevents)
        run_cfg = run_cfg.replace('{EVENTS_PER_JOB}', '%i' % args.mg_split)
        with open('%s/Cards/run_card.dat' % (workdir), "w") as outfile:
            outfile.write(run_cfg)

        with open('%s/Cards/amcatnlo_configuration.txt' % (workdir)) as amc_file:
            amc_cfg = amc_file.read()
        amc_cfg = amc_cfg.replace('{MG_PATH}', '%s' % os.path.abspath(args.mg_dir))
        amc_cfg = amc_cfg.replace('{LHAPDF_PATH}', '%s/bin/lhapdf-config' % subprocess.check_output(['scram', 'tool tag lhapdf LHAPDF_BASE']).strip())
        with open('%s/Cards/amcatnlo_configuration.txt' % (workdir), "w") as outfile:
            outfile.write(amc_cfg)
        
        base_cmd = 'cd %s' % workdir
        cmd = base_cmd
        cmd += '; echo "3" | ./bin/generate_events --nb_core=%i' % args.cores

        job_mgr.job_queue.append(cmd)

    if args.step in ['clean']:
        os.system('rm -r %s/SubProcesses %s/Events/run_01/alllogs_*' % (workdir, workdir))
        
    blocks = int(ceil(float(args.nevents) / float(args.split)))

    if args.step in ['gen', 'ntuple']:
        key = 'bbH_%s' % (MASS)

        for b in xrange(blocks):
            outdir = '$PWD/'+key
            if args.step == 'gen':
                if args.usetmp:
                    outdir = '$TMPDIR'
                cmd = 'cmsRun fromEDM2GEN_madgraph_amcatnlo.py input=%s/lhe_events.root output=%s/gen_events_%i.root seed=%i events=%i offset=%i mass=%f higgs=%s' % (key, outdir, b, b, args.split, args.split*b, float(MASS), '25')
                if args.upload is not None:
                    cmd += '; gfal-copy -f file://%s/gen_events_%i.root %s/%s/gen_events_%i.root' % (outdir, b, args.upload, key, b)
                    cmd += '; rm %s/gen_events_%i.root' % (outdir, b)
                job_mgr.job_queue.append(cmd)
            if args.step == 'ntuple':
                indir = outdir
                if args.download is not None:
                    indir = args.download + '/' + key
                cmd = 'cmsRun gen_ntuple_from_gen_cfg.py input=%s/gen_events_%i.root output=%s/EventTree_%i.root' % (indir, b, outdir, b)
                # Write the filelist if this is the first job
                if b == 0:
                    cmd += '; echo -e "'
                    files = [ ]
                    for bi in range(blocks):
                        files.append('%s/EventTree_%i.root' % (key, bi))
                    cmd += '\\n'.join(files)
                    cmd += '" &> %s.dat' % key
                job_mgr.job_queue.append(cmd)
    
job_mgr.flush_queue()

