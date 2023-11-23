Steps = {
    "DATAl1loose2018v9": {
        "isChain": True,
        "do4MC": False,
        "do4Data": True,
        "selection": '"((nElectron+nMuon)>0)"',
        "subTargets": [
            "lumiMask",
            "leptonMaker",
            "lepSel",
            "jetSelUL",
            # "CleanFatJet",
            # "rochesterDATA",
            "l2Kin",
            # "l3Kin",
            # "l4Kin",
            "trigData",
            #"formulasDATA",
            "finalSnapshot_DATA",
        ],
    },
    "DATAl1loose2022EEv11": {
        "isChain": True,
        "do4MC": False,
        "do4Data": True,
        "selection": '"((nElectron+nMuon)>0)"',
        "subTargets": [
            "lumiMask22",
            "leptonMaker",
            "lepSel2022",
            "jetSel2022",
            "l2Kin",
            "l3Kin",
            "trigData22",
            "formulasDATA",
            "finalSnapshot_DATA",
        ],
    },
    "fakeSel": {
        "isChain": True,
        "do4MC": False,
        "do4Data": True,
        "selection": '"((MET_pt < 20 || PuppiMET_pt < 20) && mtw1 < 20)"',
        "subTargets": [
            "finalSnapshot_DATA",
        ],
    },
    "fakeSelKinMC": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "selection": '"((nElectron+nMuon)>0)"',
        "subTargets": [
            "baseW",
            "trigMCnoSF",
            "l2Kin",
            "l3Kin",
            "puW",
            "formulasMCnoSF",
            "fakeSelMC",
            "finalSnapshot_MC",
        ],
    },
    "l2loose": {
        "isChain": True,
        "do4MC": True,
        "do4Data": True,
        "selection": '"(Lepton_pt.size()>1)"',
        "subTargets": [
            "finalSnapshot_MC",
        ],
    },
    "l2tightOR2022v11": {
        "isChain": True,
        "do4MC": True,
        "do4Data": True,
        "selection": '"(Lepton_pt.size()>1 && Lepton_pt[0]>18 && Lepton_pt[1]>8) && \
        (Lepton_isTightElectron_cut_Tight_HWWW[0] > 0.5    \
        || Lepton_isTightElectron_cut_Tight_HWWW_tthmva70[0] > 0.5  \
        || Lepton_isTightElectron_cut_Medium_HWWW[0] > 0.5   \
        || Lepton_isTightElectron_mvaWinter22V2Iso_WP90[0] > 0.5   \
        || Lepton_isTightElectron_mvaWinter22V2Iso_WP90_tthmva70[0] > 0.5  \
        || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5   \
        || Lepton_isTightMuon_cut_Medium_HWWW[0] > 0.5  \
        || Lepton_isTightMuon_cut_Tight_HWWW_tthmva_80[0] > 0.5   \
        || Lepton_isTightMuon_cut_Medium_HWWW_tthmva_80[0] > 0.5) && \
        (Lepton_isTightElectron_cut_Tight_HWWW[1] > 0.5   \
        || Lepton_isTightElectron_cut_Tight_HWWW_tthmva70[1] > 0.5  \
        || Lepton_isTightElectron_cut_Medium_HWWW[1] > 0.5   \
        || Lepton_isTightElectron_mvaWinter22V2Iso_WP90[1] > 0.5   \
        || Lepton_isTightElectron_mvaWinter22V2Iso_WP90_tthmva70[1] > 0.5  \
        || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5   \
        || Lepton_isTightMuon_cut_Medium_HWWW[1] > 0.5  \
        || Lepton_isTightMuon_cut_Tight_HWWW_tthmva_80[1] > 0.5   \
        || Lepton_isTightMuon_cut_Medium_HWWW_tthmva_80[1] > 0.5 ) "',
        "subTargets": [
            "finalSnapshot_MC",
        ],
    },
    "MCl1loose2022EEv12__MCCorr2022EEv12": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "selection": '"((nElectron+nMuon)>0)"',
        "subTargets": [
            "leptonMaker",
            "lepSel2022",
            "jetSel2022",
            "PromptParticlesGenVars",
            "GenVar",
            "GenLeptonMatch",
            "HiggsGenVars",
            "TopGenVars",
            "WGammaStar",
            "DressedLeptons",
            "baseW",
            #"btagPerJet_DeepJet_2018UL", ## To be computed on-the-fly
            "trigMC",
            "leptonSF",
            "puW",
            "JES_modules_22EE",
            "l2Kin",
            "l3Kin",
            "formulasMC",
            "finalSnapshot_JES",
        ]
    },
    "MCl1loose2022EEv11": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "selection": '"((nElectron+nMuon)>0)"',
        "subTargets": [
            "leptonMaker",
            "lepSel2022",
            "jetSel2022",
            "PromptParticlesGenVars",
            "GenVar",
            "GenLeptonMatch",
            "HiggsGenVars",
            "TopGenVars",
            "WGammaStar",
            "DressedLeptons",
            "finalSnapshot_MC",
        ]
    },
    "MCl1loose2018v9": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "selection": '"((nElectron+nMuon)>0)"',
        "subTargets": [
            "leptonMaker",
            "lepSel",
            "jetSelUL",
            "PromptParticlesGenVars",
            "GenVar",
            "GenLeptonMatch",
            "HiggsGenVars",
            "TopGenVars",
            "WGammaStar",
            "DressedLeptons",
        ]
        # 'wwNLL','ggHTheoryUncertainty', 'qqHTheoryUncertainty', 'EFTGen'],
    },
    "MCCorr2022EEv11": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "baseW",
            "btagPerJet_DeepJet_2018UL",
            "trigMC",
            "leptonSF",
            "l2Kin",
            "l3Kin",
            "puW",
            "JES_modules_22EE",
            "formulasMC",
            #"finalSnapshot_MC",
            "finalSnapshot_JES",
        ],
    },
    "MCCorr2018v9": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "baseW",
            # "JES_modules_18UL",
            # "JERsMCUL",
            # # "FatJERsMCUL",
            "btagPerJet_DeepCSV_2018UL",
            "btagPerJet_DeepJet_2018UL",
            # "JetPUID_SF_UL",
            # "rochesterMC",
            "trigMC",
            # "leptonSF",
            # "puW",
            "l2Kin",
            # # "l3Kin",
            # # "l4Kin",
            # "formulasMC",
            # # "EmbeddingVeto",
            # # "wwNLOEWK",
            # # "wwNLOEWK2",
            # # "wzNLOEWK",
            # # "zzNLOEWK",
            # # "zNLOEWK",
            # # "wNLOEWK",
            # # "qqHTheoryUncertainty",
            # # "CleanFatJet",
            # # "BoostedWtagSF",
            # "leptonMVAFiller",
        ],
    },
    "MCFull2018v9": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "MCl1loose2018v9",
            "MCCorr2018v9",
            "finalSnapshot_MC",
        ],
    },
    "leptonMaker": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LeptonMaker",
        "declare": "leptonMaker = lambda : LeptonMaker()",
        "module": "leptonMaker()",
    },
    "lepSel": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LeptonSel",
        "declare": 'leptonSel = lambda : LeptonSel("Loose", 1, "Full2018v9")',
        "module": "leptonSel()",
    },
    "lepSel2022":{
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LeptonSel",
        "declare": 'leptonSel = lambda : LeptonSel("Loose", 1, "Full2022EEv11")',
        "module": "leptonSel()",
    },
    "jetSelUL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.JetSel",
        # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7, UL2016fix=False "
        "declare": 'jetSel = lambda : JetSel(2,"loose",15.0,4.7,False)',
        "module": "jetSel()",
    },
    "jetSel2022": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.JetSel",
        # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7, UL2016fix=False "                                                                                                                                 
        "declare": 'jetSel = lambda : JetSel(2,"loose",15.0,4.7,False)',
        "module": "jetSel()",
    },
    "fakeSelMC": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import":  "mkShapesRDF.processor.modules.FakeSelMC",
        "declare": "fakeSel = lambda : FakeSelMC()",
        "module":  "fakeSel()",
    },
    "lumiMask": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LumiMask",
        "declare": "lumiMask = lambda : LumiMask(lumiFile)",
        "module": "lumiMask()",
    },
    "lumiMask22": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LumiMask",
        "declare": "lumiMask = lambda : LumiMask('/afs/cern.ch/work/s/sblancof/private/Run3Analysis/mkShapesRDF/mkShapesRDF/processor/data/certification/Cert_Collisions2022_355100_362760_Golden.json')",
        "module": "lumiMask()",
    },
    "PromptParticlesGenVars": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.PromptParticlesGenVarsProducer",
        "declare": "PromptParticlesGenVars = lambda : PromptParticlesGenVarsProducer()",
        "module": "PromptParticlesGenVars()",
    },
    "GenVar": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.GenVarProducer",
        "declare": "GenVar = lambda : GenVarProducer()",
        "module": "GenVar()",
    },
    "GenLeptonMatch": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.GenLeptonMatchProducer",
        "declare": "GenLeptonMatch = lambda : GenLeptonMatchProducer()",
        "module": "GenLeptonMatch()",
    },
    "HiggsGenVars": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.HiggsGenVarsProducer",
        "declare": "HiggsGenVars = lambda : HiggsGenVarsProducer()",
        "module": "HiggsGenVars()",
    },
    "TopGenVars": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.TopGenVarsProducer",
        "declare": "TopGenVars = lambda : TopGenVarsProducer()",
        "module": "TopGenVars()",
    },
    "WGammaStar": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.WGammaStarProducer",
        "declare": "WGammaStar = lambda : WGammaStarProducer()",
        "module": "WGammaStar()",
    },
    "DressedLeptons": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.DressedLeptonProducer",
        "declare": "DressedLeptons = lambda : DressedLeptonProducer(0.3)",
        "module": "DressedLeptons()",
    },
    "baseW": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.BaseW",
        "declare": "baseW = lambda : BaseW(sampleName, files, xs_db, RPLME_genEventSumw)",
        "module": "baseW()",
    },
    "JES_modules_18UL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.JMECalculator",
        "declare": 'jmeCalculator = lambda : JMECalculator("Summer19UL18_V5_MC", "Summer19UL18_JRV2_MC", \
            jet_object="AK4PFchs", do_Jets=True, do_MET=True, do_JER=False, store_nominal=False, store_variations=True)',
        "module": "jmeCalculator()",
    },
    "JES_modules_22EE": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.JMECalculator",
        "declare": 'jmeCalculator = lambda : JMECalculator("Summer22EEPrompt22_V1_MC", "Summer22EEPrompt22_JRV1_MC", \
            jet_object="AK4PFPuppi", do_Jets=True, do_MET=True, do_Unclustered=True, met_collections = ["PuppiMET", "MET", "RawMET"],\
            do_JER=True, store_nominal=True, store_variations=True)',
        "module": "jmeCalculator()",
    },
    "l2Kin": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.l2KinProducer",
        "declare": "l2Kin = lambda : l2KinProducer()",
        "module": "l2Kin()",
    },
    "l3Kin": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.l3KinProducer",
        "declare": "l3Kin = lambda : l3KinProducer()",
        "module": "l3Kin()",
    },
    "l4Kin": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.l4KinProducer",
        "declare": "l4Kin = lambda : l4KinProducer()",
        "module": "l4Kin()",
    },
    "puW": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.runDependentPuWRun3",
        "declare": "puWeight = lambda : runDependentPuWRun3('Full2022EEv11', files)",
        "module": "puWeight()",
    },
    "leptonSF": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LeptonSF",
        "declare": "leptonSF = lambda : LeptonSF('Full2022EEv11')",
        "module": "leptonSF()",
    },
    "formulasDATA": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.formulasToAdd_DATA_Full2022EEv11",
        "declare": "formulasDATA = lambda : formulasToAdd_DATA_Full2022EEv11()",
        "module": "formulasDATA()",
    },
    "formulasMC": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.formulasToAdd_MC_Full2022EEv11",
        "declare": "formulasMC = lambda : formulasToAdd_MC_Full2022EEv11()",
        "module": "formulasMC()",
    },
    "formulasMCnoSF": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.formulasToAdd_MCnoSF_Full2022EEv11",
        "declare": "formulasMC = lambda : formulasToAdd_MCnoSF_Full2022EEv11()",
        "module": "formulasMC()",
    },
    "btagPerJet_DeepCSV_2018UL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.btagSFProducerLatinos",
        "declare": 'btagPerJet_DeepCSV_2018UL = lambda : btagSFProducerLatinos(2018, "deepCSV", ["shape"], "shape", "RPLME_FW/processor/data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz", ["jes","jesAbsolute","jesAbsolute_2018","jesBBEC1","jesBBEC1_2018","jesEC2","jesEC2_2018","jesFlavorQCD","jesHF","jesHF_2018","jesRelativeBal","jesRelativeSample_2018"])',
        "module": "btagPerJet_DeepCSV_2018UL()",
    },
    "btagPerJet_DeepJet_2018UL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.btagSFProducerLatinos",
        "declare": 'btagPerJet_DeepJet_2018UL = lambda : btagSFProducerLatinos(2018, "deepJet", ["shape"], "shape", "RPLME_FW/processor/data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz", ["jes","jesAbsolute","jesAbsolute_2018","jesBBEC1","jesBBEC1_2018","jesEC2","jesEC2_2018","jesFlavorQCD","jesHF","jesHF_2018","jesRelativeBal","jesRelativeSample_2018"])',
        "module": "btagPerJet_DeepJet_2018UL()",
    },
    "trigMC": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.TrigMaker",
        "declare": 'trigMC = lambda : TrigMaker("Full2022EEv11", isData=False, keepRunP=False)',
        "module": "trigMC()",
    },
    "trigMCnoSF": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.TrigMaker",
        "declare": 'trigMC = lambda : TrigMaker("Full2022EEv11", isData=True, keepRunP=False)',
        "module": "trigMC()",
    },
    "trigData": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.TrigMaker",
        "declare": 'trigData = lambda : TrigMaker("Full2018v9", isData=True, keepRunP=False)',
        "module": "trigData()",
    },
    "trigData22": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.TrigMaker",
        "declare": 'trigData = lambda : TrigMaker("Full2022EEv11", isData=True, keepRunP=False)',
        "module": "trigData()",
    },
    "finalSnapshot_MC": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='RPLME_OUTPUTFILENAME', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=True, splitVariations=False, storeNominals=True )",
        "module": "snapshot()",
    },
    "finalSnapshot_Variations": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='RPLME_OUTPUTFILENAME', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=True, splitVariations=True, storeNominals=False )",
        "module": "snapshot()",
    },
    "finalSnapshot_DATA": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='RPLME_OUTPUTFILENAME', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=True, splitVariations=False, storeNominals=True )",
        "module": "snapshot()",
    },
    "finalSnapshot_JES": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='RPLME_OUTPUTFILENAME', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=True, splitVariations=True, storeNominals=True,\
                outputMap={'JES':['JER_0', 'JER_1', 'JER_2', 'JER_3', 'JER_4', 'JER_5', 'JESCorrelationGroupbJES', 'JESCorrelationGroupIntercalibration', 'JESFlavorPureQuark', 'JESFlavorPureGluon', 'JESFlavorPhotonJet', 'JESFlavorZJet', 'JESTotalNoFlavorNoTime', 'JESCorrelationGroupFlavor', 'JESTotalNoTime', 'JESTotalNoFlavor', 'JESTotal', 'JESSubTotalMC', 'JESSubTotalAbsolute', 'JESSubTotalScale', 'JESFlavorPureCharm', 'JESSubTotalPt', 'JESSubTotalPileUp', 'JESPileUpMuZero', 'JESCorrelationGroupUncorrelated', 'JESPileUpEnvelope', 'JESRelativeJERHF', 'JESRelativePtHF', 'JESRelativeJEREC2','JESSubTotalRelative', 'JESRelativeStatFSR', 'JESRelativeJEREC1', 'JESTimePtEta', 'JESFragmentation', 'JESFlavorQCD', 'JESAbsoluteMPFBias', 'JESRelativePtEC1', 'JESAbsoluteFlavMap', 'JESSinglePionECAL', 'JESAbsoluteScale', 'JESSinglePionHCAL', 'JESRelativeFSR', 'JESFlavorPureBottom', 'JESPileUpPtEC1', 'JESPileUpDataMC', 'JESAbsoluteStat', 'JESRelativePtEC2', 'JESPileUpPtEC2', 'JESRelativeBal', 'JESAbsoluteSample', 'JESRelativeSample', 'JESRelativePtBB', 'JESRelativeStatEC', 'JESRelativeStatHF', 'JESPileUpPtRef', 'JESCorrelationGroupMPFInSitu', 'JESPileUpPtBB', 'JESPileUpPtHF'], 'MET':['JER_0', 'JER_1', 'JER_2', 'JER_3', 'JER_4', 'JER_5', 'JESCorrelationGroupbJES', 'JESCorrelationGroupIntercalibration', 'JESFlavorPureQuark', 'JESFlavorPureGluon', 'JESFlavorPhotonJet', 'JESFlavorZJet', 'JESTotalNoFlavorNoTime', 'JESCorrelationGroupFlavor', 'JESTotalNoTime', 'JESTotalNoFlavor', 'JESTotal', 'JESSubTotalMC', 'JESSubTotalAbsolute', 'JESSubTotalScale', 'JESFlavorPureCharm', 'JESSubTotalPt', 'JESSubTotalPileUp', 'JESPileUpMuZero', 'JESCorrelationGroupUncorrelated', 'JESPileUpEnvelope', 'JESRelativeJERHF', 'JESRelativePtHF', 'JESRelativeJEREC2', 'JESSubTotalRelative', 'JESRelativeStatFSR', 'JESRelativeJEREC1', 'JESTimePtEta', 'JESFragmentation', 'JESFlavorQCD', 'JESAbsoluteMPFBias', 'JESRelativePtEC1', 'JESAbsoluteFlavMap', 'JESSinglePionECAL', 'JESAbsoluteScale', 'JESSinglePionHCAL', 'JESRelativeFSR', 'JESFlavorPureBottom', 'JESPileUpPtEC1', 'JESPileUpDataMC', 'JESAbsoluteStat', 'JESRelativePtEC2', 'JESPileUpPtEC2', 'JESRelativeBal', 'JESAbsoluteSample', 'JESRelativeSample', 'JESRelativePtBB', 'JESRelativeStatEC', 'JESRelativeStatHF', 'JESPileUpPtRef', 'JESCorrelationGroupMPFInSitu', 'JESPileUpPtBB', 'JESPileUpPtHF'],} )",
        "module": "snapshot()",
    },
    "histogram": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.Histogram",
        "declare": "histogram = lambda : Histogram( \
                outputFilename='output2.root', \
                variables=[(('mjj', 'mjj', 100, 10, 1000), 'new_fw_mjj', 'baseW * genWeight')] \
                    )",
        "module": "histogram()",
    },
}
