from WMCore.Configuration import Configuration
from multiprocessing import Process
config = Configuration()

PROD='miniaod-prod-100517'

config.section_('General')
config.General.workArea=PROD

config.section_('JobType')
config.JobType.scriptExe = 'jobScript.sh'
config.JobType.psetName = 'miniaod_step1_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['miniaod.root']
config.JobType.inputFiles = ['jobScript.sh', 'miniaod_step2_cfg.py', 'miniaod_step3_cfg.py']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500

config.section_('Data')
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 1
config.Data.splitting = 'FileBased'
config.Data.publication = True
config.Data.ignoreLocality=True
config.Data.outputDatasetTag = PROD
config.Data.inputDBS = 'phys03'

config.section_('User')
config.User.voGroup = 'dcms'


config.section_('Site')
config.Site.storageSite = 'T2_DE_DESY'
config.Site.whitelist = ['T2_CH_CERN', 'T1_US_FNAL', 'T2_DE_DESY']
config.Site.blacklist = ['T2_US_Purdue']

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

    #primary = 'SUSYGluGluToBBHToTauTau_M-%s_TuneCUETP8M1_13TeV-amcatnlo-pythia8'
    tasks=[
            ('SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-100517-6afa54f6ff8db0c7f2e5ef660af07239/USER')
            ]

    for task in tasks:
        #print task
        #continue
        print task[0]
        config.General.requestName = task[0]
        config.Data.inputDataset = task[1]
        print config
        #continue
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()



