# Auto generated configuration file
# using: 
# Revision: 1.20 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/ThirteenTeV/WH_ZH_HToTauTau_M_125_TuneZ2star_13TeV_pythia6_cff.py --fileout file:HIG-Fall13-00001.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions POSTLS162_V1::All --step GEN,SIM --magField 38T_PostLS1 --geometry Extended2015 --python_filename HIG-Fall13-00001_1_cfg.py --no_exec -n 29
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('python')
options.register('output','',VarParsing.multiplicity.singleton,VarParsing.varType.string,"type parameter")
options.register('input','',VarParsing.multiplicity.singleton,VarParsing.varType.string,"type parameter")
options.register('higgs','',VarParsing.multiplicity.singleton,VarParsing.varType.string,"type parameter")
options.register('events','',VarParsing.multiplicity.singleton,VarParsing.varType.int,"type parameter")
options.register('offset','',VarParsing.multiplicity.singleton,VarParsing.varType.int,"type parameter")
options.register('seed','',VarParsing.multiplicity.singleton,VarParsing.varType.int,"type parameter")
options.register('mass','',VarParsing.multiplicity.singleton,VarParsing.varType.float,"type parameter")

options.parseArguments()
#outputfilename = "file:%s_%s.root"%(options.output.replace(".root",""),options.jobnum)
outputfilename = "file:%s"%(options.output)
inputfilename = "file:%s"%(options.input)

process = cms.Process('SIM')
#with open("slha.slha","r") as slhafile:
#    SLHA="".join(slhafile.readlines())


# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.events)
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring([inputfilename]),
                             skipEvents = cms.untracked.uint32(options.offset)
)


process.options = cms.untracked.PSet(

)

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.RandomNumberGeneratorService.generator.initialSeed = options.seed

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('PYTHIA6 WH/ZH, H->2tau mH=125GeV with TAUOLA at 13TeV'),
    name = cms.untracked.string('$Source: /cvs/CMSSW/CMSSW/Configuration/GenProduction/python/ThirteenTeV/WH_ZH_HToTauTau_M_125_TuneZ2star_13TeV_pythia6_cff.py,v $')
)

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string(outputfilename),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
      pythia8CommonSettingsBlock,
      pythia8CUEP8M1SettingsBlock,
      pythia8aMCatNLOSettingsBlock,
      processParameters = cms.vstring(
        'TimeShower:nPartonsInBorn = 2', #number of coloured particles (before resonance decays) in born matrix element
        #'Higgs:useBSM = on',
        'SLHA:useDecayTable = off',
        '%s:onMode = off' % options.higgs, # turn OFF all H decays
        '%s:onIfAny = 15' % options.higgs,    # turn ON H->tautau
        '%s:m0 = %g' % (options.higgs, options.mass)
        ),
      parameterSets = cms.vstring('pythia8CommonSettings',
        'pythia8CUEP8M1Settings',
        'pythia8aMCatNLOSettings',
        'processParameters'
        )
      )
    )

#print process.generator.PythiaParameters.processParameters

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)


# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)


# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
