# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: MCDBtoEDM --conditions MCRUN2_71_V1::All -s NONE --eventcontent RAWSIM --datatier GEN --filein file:/tmp/ytakahas/events.lhe --no_exec -n 1
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('python')
options.register('input','', VarParsing.multiplicity.list, VarParsing.varType.string, "input files")
options.parseArguments()

process = cms.Process('LHE')

# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring(options.input)
)

process.options = cms.untracked.PSet(

)

process.MessageLogger.cerr.FwkReport.reportEvery = 10000

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('MCDBtoEDM nevts:1'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string("lhe.root"),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
    )
)

# Additional output definition

# Other statements

# Path and EndPath definitions
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.RAWSIMoutput_step)

