from UserCode.ICHiggsTauTau.jobs import Jobs
import argparse
import os
import ROOT
from math import ceil
from array import array

job_mgr = Jobs()
parser = argparse.ArgumentParser()

parser.add_argument('--pwhg-dir', default='.')
parser.add_argument('-n', '--nevents', default=10000, type=int)
parser.add_argument('--split', default=-1, type=int)
parser.add_argument('-m', '--mass', default='500')
parser.add_argument('-t', '--tanb', default='15')
parser.add_argument('-c', '--contribution', default='t:t')
parser.add_argument('-H', '--higgs', default='H', choices=['H', 'A'])
parser.add_argument('--step', default='none', choices=['none', 'lhe', 'gen', 'ntuple'])
parser.add_argument('--upload', default=None)
parser.add_argument('--download', default=None)
parser.add_argument('--usetmp', action='store_true')

job_mgr.attach_job_args(parser)
args = parser.parse_args()
job_mgr.set_args(args)

if args.split == -1:
    args.split = args.nevents


higgstype = {
    'H': '2',
    'A': '3'
    }

mass = []
qt = []
qb = []
qtb = []

with open('scales-higgs-mass-scan.dat') as scales_file:
    for line in scales_file:
        m, ht, hb, htb = line.split()
        mass.append(float(m))
        qt.append(float(ht))
        qb.append(float(hb))
        qtb.append(float(htb))
gr = {}
gr['t'] = ROOT.TGraph(len(mass), array('d', mass), array('d', qt))
gr['b'] = ROOT.TGraph(len(mass), array('d', mass), array('d', qb))
gr['tb'] = ROOT.TGraph(len(mass), array('d', mass), array('d', qtb))

if args.step == 'lhe':

    with open('powheg.input') as pwhg_file:
        pwhg_cfg = pwhg_file.read()

    pwhg_cfg = pwhg_cfg.replace('{EVENTS}', str(args.nevents))
    pwhg_cfg = pwhg_cfg.replace('{MASS}', args.mass)
    pwhg_cfg = pwhg_cfg.replace('{TANB}', args.tanb)
    pwhg_cfg = pwhg_cfg.replace('{HIGGSTYPE}', higgstype[args.higgs])

    base_cmd = 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%s/lib' % args.pwhg_dir

    for task in args.contribution.split(','):
        cont, scale = task.split(':')

        key = '%s_%s_%s_%s_%s' % (args.higgs, args.mass, args.tanb, cont, scale)
        
        cfg = pwhg_cfg
        cfg = cfg.replace('{HFACT}', str(int(round(gr[scale].Eval(float(args.mass))))))
        if cont == 't':
            cfg += 'nobot 1\n'
        if cont == 'b':
            cfg += 'notop 1\n'
    

        #if os.path.isdir(key):
        #  print 'Error, directory %s already exists!' % key
        #  sys.exit(1)

        os.system('mkdir -p %s' % key)

        with open(os.path.join(key,'powheg.input'), "w") as outfile:
            outfile.write(cfg)

        cmd = base_cmd
        cmd += '; pushd %s; %s/pwhg_main powheg.input' % (key, args.pwhg_dir)
        cmd += '; popd; cmsRun fromLHE2EDM.py input=%s/pwgevents.lhe output=%s/lhe_events.root' % (key, key)
        job_mgr.job_queue.append(cmd)

    job_mgr.flush_queue()

blocks = int(ceil(float(args.nevents) / float(args.split)))

if args.step in ['gen', 'ntuple']:
    for task in args.contribution.split(','):
        cont, scale = task.split(':')
        key = '%s_%s_%s_%s_%s' % (args.higgs, args.mass, args.tanb, cont, scale)

        for b in xrange(blocks):
            outdir = '$PWD/'+key
            if args.step == 'gen':
                if args.usetmp:
                    outdir = '$TMPDIR'
                cmd = 'cmsRun fromEDM2GEN_powheg.py input=%s/lhe_events.root output=%s/gen_events_%i.root seed=%i events=%i offset=%i mass=%f' % (key, outdir, b, b, args.split, args.split*b, float(args.mass))
                if args.upload is not None:
                    cmd += '; gfal-copy file://%s/gen_events_%i.root %s/%s/gen_events_%i.root' % (outdir, b, args.upload, key, b)
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


