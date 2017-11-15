from WMCore.Configuration import Configuration
from multiprocessing import Process
config = Configuration()

PROD='gen-prod-260917'

config.section_('General')
config.General.workArea=PROD

config.section_('JobType')
config.JobType.psetName = 'gensim_prod_cfg.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.outputFiles = ['gen.root']
config.JobType.pyCfgParams = []

config.section_('Data')
config.Data.unitsPerJob = 1
config.Data.totalUnits = 1 
config.Data.splitting = 'EventBased'
config.Data.publication = True
config.Data.ignoreLocality=False
config.Data.outputDatasetTag = PROD
config.Data.outputPrimaryDataset = ''
config.Data.outLFNDirBase='/store/group/cmst3/group/htautau/%s' % PROD

config.section_('User')


config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = ['T2_DE_DESY']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print hte.headers

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################
    tasks=[
        #('OldAcc_1_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/OldAcc_1_M-700_tarball.tar.xz', 2000000, 20000),
        #('OldAcc_2_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/OldAcc_2_M-700_tarball.tar.xz', 2000000, 20000),
        #('OldAcc_3_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/OldAcc_3_M-700_tarball.tar.xz', 2000000, 20000),
        #('OldAcc_4_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/OldAcc_4_M-700_tarball.tar.xz', 2000000, 20000),
        #('OldAcc_5_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/OldAcc_5_M-700_tarball.tar.xz', 2000000, 20000),
        ('NewAcc_1_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/NewAcc_1_M-700_tarball.tar.xz', 2000000, 20000),
        ('NewAcc_2_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/NewAcc_2_M-700_tarball.tar.xz', 2000000, 20000),
        ('NewAcc_3_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/NewAcc_3_M-700_tarball.tar.xz', 2000000, 20000),
        ('NewAcc_4_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/NewAcc_4_M-700_tarball.tar.xz', 2000000, 20000),
        ('NewAcc_5_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'root://eoscms.cern.ch//store/cmst3/user/agilbert/NewAcc_5_M-700_tarball.tar.xz', 2000000, 20000),
            ]

    for task in tasks:
        #print task
        #continue
        print task[0]
        config.General.requestName = task[0]
        config.Data.outputPrimaryDataset = task[0]
        config.JobType.pyCfgParams = ['gridpack=%s' % task[1]]
        config.Data.totalUnits = task[2] 
        config.Data.unitsPerJob = task[3]
        print config
        #continue
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()



