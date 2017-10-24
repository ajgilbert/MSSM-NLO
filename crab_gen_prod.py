from WMCore.Configuration import Configuration
from multiprocessing import Process
config = Configuration()

PROD='prod_040817'

config.section_('General')
config.General.workArea=PROD
#config.General.requestName = ''


config.section_('JobType')
config.JobType.psetName = ''
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['EventTree.root']
#config.JobType.inputFiles = ['Summer15_V5_MC.db']
#config.JobType.pyCfgParams = ['release=80XMINIAOD','isData=1', 'globalTag=80X_dataRun2_Prompt_v8']
#config.JobType.maxMemoryMB = 2499

config.section_('Data')
#config.Data.inputDataset = ''
config.Data.unitsPerJob = 50000
config.Data.splitting = 'EventAwareLumiBased'
config.Data.publication = False
#config.Data.runRange = '271036-274240'
config.Data.ignoreLocality=False
config.Data.outLFNDirBase='/store/group/cmst3/user/agilbert/%s' % PROD
config.Data.inputDBS = 'global'

config.section_('User')
config.User.voGroup = 'dcms'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T1_FR_CCIN2P3']

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
    ('SUSYGluGluToHToTauTau_M-80', '/SUSYGluGluToHToTauTau_M-80_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-90', '/SUSYGluGluToHToTauTau_M-90_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-100', '/SUSYGluGluToHToTauTau_M-100_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-110', '/SUSYGluGluToHToTauTau_M-110_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-120', '/SUSYGluGluToHToTauTau_M-120_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-130', '/SUSYGluGluToHToTauTau_M-130_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-140', '/SUSYGluGluToHToTauTau_M-140_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-160', '/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-180', '/SUSYGluGluToHToTauTau_M-180_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-200', '/SUSYGluGluToHToTauTau_M-200_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-250', '/SUSYGluGluToHToTauTau_M-250_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-300', '/SUSYGluGluToHToTauTau_M-300_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-350', '/SUSYGluGluToHToTauTau_M-350_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-400', '/SUSYGluGluToHToTauTau_M-400_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-450', '/SUSYGluGluToHToTauTau_M-450_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-500', '/SUSYGluGluToHToTauTau_M-500_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-600', '/SUSYGluGluToHToTauTau_M-600_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-700', '/SUSYGluGluToHToTauTau_M-700_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-800', '/SUSYGluGluToHToTauTau_M-800_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-900', '/SUSYGluGluToHToTauTau_M-900_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-1000', '/SUSYGluGluToHToTauTau_M-1000_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-1200', '/SUSYGluGluToHToTauTau_M-1200_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-1400', '/SUSYGluGluToHToTauTau_M-1400_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-1500', '/SUSYGluGluToHToTauTau_M-1500_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-1600', '/SUSYGluGluToHToTauTau_M-1600_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-1800', '/SUSYGluGluToHToTauTau_M-1800_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-2000', '/SUSYGluGluToHToTauTau_M-2000_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-2300', '/SUSYGluGluToHToTauTau_M-2300_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-2600', '/SUSYGluGluToHToTauTau_M-2600_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-2900', '/SUSYGluGluToHToTauTau_M-2900_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
    ('SUSYGluGluToHToTauTau_M-3200', '/SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global')
            ]

    tasks_bbH = [
        ('SUSYGluGluToBBHToTauTau_M-80', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-90', '/SUSYGluGluToBBHToTauTau_M-90_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-100', '/SUSYGluGluToBBHToTauTau_M-100_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-110', '/SUSYGluGluToBBHToTauTau_M-110_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-120', '/SUSYGluGluToBBHToTauTau_M-120_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        ('SUSYGluGluToBBHToTauTau_M-130', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-140', '/SUSYGluGluToBBHToTauTau_M-140_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-160', '/SUSYGluGluToBBHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-180', '/SUSYGluGluToBBHToTauTau_M-180_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        ('SUSYGluGluToBBHToTauTau_M-200', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-250', '/SUSYGluGluToBBHToTauTau_M-250_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        ('SUSYGluGluToBBHToTauTau_M-350', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-400', '/SUSYGluGluToBBHToTauTau_M-400_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-450', '/SUSYGluGluToBBHToTauTau_M-450_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-500', '/SUSYGluGluToBBHToTauTau_M-500_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-600', '/SUSYGluGluToBBHToTauTau_M-600_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        ('SUSYGluGluToBBHToTauTau_M-700', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-800', '/SUSYGluGluToBBHToTauTau_M-800_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-900', '/SUSYGluGluToBBHToTauTau_M-900_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-1000', '/SUSYGluGluToBBHToTauTau_M-1000_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        ('SUSYGluGluToBBHToTauTau_M-1200', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-1400', '/SUSYGluGluToBBHToTauTau_M-1400_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-1600', '/SUSYGluGluToBBHToTauTau_M-1600_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        ('SUSYGluGluToBBHToTauTau_M-1800', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-2000', '/SUSYGluGluToBBHToTauTau_M-2000_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-2300', '/SUSYGluGluToBBHToTauTau_M-2300_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-2600', '/SUSYGluGluToBBHToTauTau_M-2600_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        #('SUSYGluGluToBBHToTauTau_M-2900', '/SUSYGluGluToBBHToTauTau_M-2900_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        ('SUSYGluGluToBBHToTauTau_M-3200', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_cfg.py', 'global'),
        ('SUSYGluGluToBBHToTauTau_M-80-mg', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-130-mg', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-200-mg', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-350-mg', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-700-mg', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-120-mg', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-1800-mg', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-3200-mg', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-miniaod-prod-250517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-80-mg-qlo', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-80-mg-qhi', '/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-130-mg-qlo', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-130-mg-qhi', '/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-200-mg-qlo', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-200-mg-qhi', '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-350-mg-qlo', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-350-mg-qhi', '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-700-mg-qlo', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-700-mg-qhi', '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-120-mg-qlo', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-120-mg-qhi', '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-1800-mg-qlo', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-1800-mg-qhi', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-3200-mg-qlo', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshDown/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-3200-mg-qhi', '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-amcatnlo-pythia8-QshUp/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ]

    tasks_new = [
        ('SUSYGluGluToBBHToTauTau_M-1800-private', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8/agilbert-miniaod-prod-150517-28028af67189b3de7224b79195bd0e1d/USER', 'gen_ntuple_from_miniaod_mg_cfg.py', 'phys03'),
        ('SUSYGluGluToBBHToTauTau_M-1800-official', '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'gen_ntuple_from_miniaod_mg_cfg.py', 'global'),
    ]

    for task in tasks_new:
        #print task
        #continue
        print task[0]
        config.General.requestName = task[0]
        config.Data.inputDataset = task[1]
        config.JobType.psetName = task[2]
        config.Data.inputDBS = task[3]
        print config
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()



