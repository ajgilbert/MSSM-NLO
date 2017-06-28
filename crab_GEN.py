from WMCore.Configuration import Configuration
from multiprocessing import Process
config = Configuration()

PROD='gen-prod-150517'

config.section_('General')
config.General.workArea=PROD

config.section_('JobType')
config.JobType.psetName = 'fromEDM2GEN_madgraph_amcatnlo_crab.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['gensim.root']

config.section_('Data')
config.Data.unitsPerJob = 500
config.Data.splitting = 'EventAwareLumiBased'
config.Data.publication = True
config.Data.ignoreLocality=True
config.Data.outputDatasetTag = PROD
config.Data.inputDBS = 'phys03'

config.section_('User')
config.User.voGroup = 'dcms'


config.section_('Site')
config.Site.storageSite = 'T2_DE_DESY'
config.Site.whitelist = ['T2_*', 'T1_*']
config.Site.blacklist= ['T1_IT_CNAF', 'T2_UK_London_Brunel']

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
            #('SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-lhe-prod-100517-3f22eb42fbc8c953391827da6f10333b/USER', '700')
            #(primary % '80', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '80'),
            #(primary % '130', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '130'),
            #(primary % '200', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '200'),
            #(primary % '350', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '350'),
            #(primary % '700', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '700'),
            #(primary % '1200', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '1200'),
            #(primary % '1800', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '1800'),
            (primary % '3200', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '3200'),
            #(primaryLo % '80', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '80'),
            #(primaryLo % '130', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '130'),
            #(primaryLo % '200', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '200'),
            #(primaryLo % '350', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '350'),
            #(primaryLo % '700', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '700'),
            #(primaryLo % '1200', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '1200'),
            #(primaryLo % '1800', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '1800'),
            #(primaryLo % '3200', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '3200'),
            #(primaryHi % '80', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '80'),
            #(primaryHi % '130', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '130'),
            #(primaryHi % '200', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '200'),
            #(primaryHi % '350', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '350'),
            #(primaryHi % '700', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '700'),
            #(primaryHi % '1200', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '1200'),
            #(primaryHi % '1800', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '1800'),
            #(primaryHi % '3200', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-lhe-prod-150517-3f22eb42fbc8c953391827da6f10333b/USER', '3200'),
            ]

    for task in tasks:
        #print task
        #continue
        print task[0]
        config.General.requestName = task[0]
        config.Data.inputDataset = task[1]
        config.JobType.pyCfgParams = ['mass=%s' % task[2]]
        print config
        #continue
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()



