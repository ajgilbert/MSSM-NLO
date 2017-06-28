from WMCore.Configuration import Configuration
from multiprocessing import Process
config = Configuration()

PROD='miniaod-prod-250517'

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
config.Site.whitelist = ['T2_CH_CERN', 'T1_US_FNAL', 'T2_DE_DESY', 'T1_DE_KIT']
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

    primary = 'SUSYGluGluToBBHToTauTau_M-%s_TuneCUETP8M1_13TeV-amcatnlo-pythia8'
    primaryLo = 'SUSYGluGluToBBHToTauTau_M-%s_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown'
    primaryHi = 'SUSYGluGluToBBHToTauTau_M-%s_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp'
    tasks=[
            #('SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-100517-6afa54f6ff8db0c7f2e5ef660af07239/USER')
            #(primary % '80', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-150517-2c7d5ffa4a12d45480fa2f6938c22fd1/USER'),
            #(primary % '130', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-150517-e750ca311ede1e15f7c8635adb3f1a6a/USER'),
            #(primary % '200', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-150517-716c615b266d241ae56be8cea69cedd1/USER'),
            #(primary % '350', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-150517-19e4fe80c91047dac2f68c37702b624f/USER'),
            #(primary % '700', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-150517-6afa54f6ff8db0c7f2e5ef660af07239/USER'),
            #(primary % '1200', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-150517-a5fc9c90fbad422f376bbdacf55c4ede/USER'),
            #(primary % '1800', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-150517-f72897aeaf95b5b03fb8da2a01ed0647/USER'),
            (primary % '3200', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-gen-prod-150517-5f8dc5341f27bacc9a153504e6e7148f/USER'),
            #(primaryLo % '80', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-gen-prod-150517-2c7d5ffa4a12d45480fa2f6938c22fd1/USER'),
            #(primaryLo % '130', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-gen-prod-150517-e750ca311ede1e15f7c8635adb3f1a6a/USER'),
            #(primaryLo % '200', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-gen-prod-150517-716c615b266d241ae56be8cea69cedd1/USER'),
            #(primaryLo % '350', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-gen-prod-150517-19e4fe80c91047dac2f68c37702b624f/USER'),
            #(primaryLo % '700', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-gen-prod-150517-6afa54f6ff8db0c7f2e5ef660af07239/USER'),
            #(primaryLo % '1200', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-gen-prod-150517-a5fc9c90fbad422f376bbdacf55c4ede/USER'),
            #(primaryLo % '1800', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-gen-prod-150517-f72897aeaf95b5b03fb8da2a01ed0647/USER'),
            #(primaryLo % '3200', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-gen-prod-150517-5f8dc5341f27bacc9a153504e6e7148f/USER'),
            #(primaryHi % '80', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-gen-prod-150517-2c7d5ffa4a12d45480fa2f6938c22fd1/USER'),
            #(primaryHi % '130', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-gen-prod-150517-e750ca311ede1e15f7c8635adb3f1a6a/USER'),
            #(primaryHi % '200', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-gen-prod-150517-716c615b266d241ae56be8cea69cedd1/USER'),
            #(primaryHi % '350', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-gen-prod-150517-19e4fe80c91047dac2f68c37702b624f/USER'),
            #(primaryHi % '700', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-gen-prod-150517-6afa54f6ff8db0c7f2e5ef660af07239/USER'),
            #(primaryHi % '1200', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-gen-prod-150517-a5fc9c90fbad422f376bbdacf55c4ede/USER'),
            #(primaryHi % '1800', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-gen-prod-150517-f72897aeaf95b5b03fb8da2a01ed0647/USER'),
            #(primaryHi % '3200', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-gen-prod-150517-5f8dc5341f27bacc9a153504e6e7148f/USER')
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



