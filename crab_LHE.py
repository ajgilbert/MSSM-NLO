from WMCore.Configuration import Configuration
from multiprocessing import Process
config = Configuration()

PROD='lhe-prod-100517'

config.section_('General')
config.General.workArea=PROD

config.section_('JobType')
config.JobType.psetName = 'fromLHE2EDM_crab.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.outputFiles = ['lhe.root']

config.section_('Data')
config.Data.unitsPerJob = 1
config.Data.totalUnits = 1 
config.Data.splitting = 'EventBased'
config.Data.publication = True
config.Data.ignoreLocality=False
config.Data.outputDatasetTag = PROD
config.Data.outputPrimaryDataset = ''

config.section_('User')
config.User.voGroup = 'dcms'


config.section_('Site')
config.Site.storageSite = 'T2_DE_DESY'
config.Site.whitelist = ['T2_DE_DESY']

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
    tasks=[
            (primary % '700', 'root://dcache-cms-xrootd.desy.de//store/user/agilbert/madgraph_amcatnlo/bbH/700/events.lhe', 500000, 100000)
            ]

    for task in tasks:
        #print task
        #continue
        print task[0]
        config.General.requestName = task[0]
        config.Data.outputPrimaryDataset = task[0]
        config.JobType.pyCfgParams = ['input=%s' % task[1]]
        config.Data.totalUnits = task[2] 
        config.Data.unitsPerJob = task[3]
        print config
        #continue
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()



