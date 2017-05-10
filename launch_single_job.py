from UserCode.ICHiggsTauTau.jobs import Jobs
import argparse

job_mgr = Jobs()
parser = argparse.ArgumentParser()

parser.add_argument('--cmd', default='')

job_mgr.attach_job_args(parser)
args = parser.parse_args()
job_mgr.set_args(args)

job_mgr.job_queue.append(args.cmd)
    
job_mgr.flush_queue()


