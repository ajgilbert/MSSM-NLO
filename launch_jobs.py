from UserCode.ICHiggsTauTau.jobs import Jobs
import argparse
import os
import ROOT
from array import array

job_mgr = Jobs()
parser = argparse.ArgumentParser()

parser.add_argument('--pwhg-dir', default='.')
parser.add_argument('-n', '--nevents', default=10000, type=int)
parser.add_argument('-m', '--mass', default='500')
parser.add_argument('-t', '--tanb', default='15')
parser.add_argument('-c', '--contribution', default='t:t')
parser.add_argument('-H', '--higgs', default='H', choices=['H', 'A'])

job_mgr.attach_job_args(parser)
args = parser.parse_args()
job_mgr.set_args(args)

base_cmd = 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%s/lib' % args.pwhg_dir

with open('powheg.input') as pwhg_file:
    pwhg_cfg = pwhg_file.read()

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

pwhg_cfg = pwhg_cfg.replace('{EVENTS}', str(args.nevents))
pwhg_cfg = pwhg_cfg.replace('{MASS}', args.mass)
pwhg_cfg = pwhg_cfg.replace('{TANB}', args.tanb)
pwhg_cfg = pwhg_cfg.replace('{HIGGSTYPE}', higgstype[args.higgs])

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


#print pwhg_cfg


