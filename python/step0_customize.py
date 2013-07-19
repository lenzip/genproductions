import FWCore.ParameterSet.Config as cms

def customise(process):
        process.schedule.remove(process.RAWSIMoutput_step)
        process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10000)
        return(process)

