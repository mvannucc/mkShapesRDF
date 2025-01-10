import os
from mkShapesRDF.lib.search_files import SearchFiles

mcProduction = "Summer20UL18_106x_nAODv9_Full2018v9"
dataReco = "Run2018_UL2018_nAODv9_Full2018v9"
mcSteps = "MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9"
fakeSteps = "DATAl1loose2018v9__l2loose__fakeW"
dataSteps = "DATAl1loose2018v9__l2loose__l2tightOR2018v9"

treeBaseDir = "/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano"
limitFiles = -1

useXROOTD = False

if useXROOTD:
    redirector = "root://eoscms.cern.ch/"
else:
    redirector = ""

print(treeBaseDir)


def makeMCDirectory(var=""):
    _treeBaseDir = treeBaseDir + ""
    if useXROOTD:
        _treeBaseDir = redirector + treeBaseDir
    if var == "":
        return "/".join([_treeBaseDir, mcProduction, mcSteps])
    else:
        return "/".join([_treeBaseDir, mcProduction, mcSteps + "__" + var])

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

samples = {}


s = SearchFiles()

useXROOTD = False
redirector = 'root://eoscms.cern.ch/'     # SM samples
redirector2 = 'root://eoshome-m.cern.ch/' # EFT samples

def nanoGetSampleFiles(path, name):
    _files = s.searchFiles(path, name, redirector=redirector)
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return [(name, _files)]

def nanoGetSampleFiles2(path, name):
    _files = s.searchFiles(path, name, redirector=redirector2)
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return [(name, _files)]


def CombineBaseW(samples, proc, samplelist):
    _filtFiles = list(filter(lambda k: k[0] in samplelist, samples[proc]["name"]))
    _files = list(map(lambda k: k[1], _filtFiles))
    _l = list(map(lambda k: len(k), _files))
    leastFiles = _files[_l.index(min(_l))]
    dfSmall = ROOT.RDataFrame("Runs", leastFiles)
    s = dfSmall.Sum("genEventSumw").GetValue()
    f = ROOT.TFile(leastFiles[0])
    t = f.Get("Events")
    t.GetEntry(1)
    xs = t.baseW * s

    __files = []
    for f in _files:
        __files += f
    df = ROOT.RDataFrame("Runs", __files)
    s = df.Sum("genEventSumw").GetValue()
    newbaseW = str(xs / s)
    weight = newbaseW + "/baseW"

    for iSample in samplelist:
        addSampleWeight(samples, proc, iSample, weight)


def addSampleWeight(samples, sampleName, sampleNameType, weight):
    obj = list(filter(lambda k: k[0] == sampleNameType, samples[sampleName]["name"]))[0]
    samples[sampleName]["name"] = list(
        filter(lambda k: k[0] != sampleNameType, samples[sampleName]["name"])
    )
    if len(obj) > 2:
        samples[sampleName]["name"].append(
            (obj[0], obj[1], obj[2] + "*(" + weight + ")")
        )
    else:
        samples[sampleName]["name"].append((obj[0], obj[1], "(" + weight + ")"))


################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ["A", "Run2018A-UL2018-v1"],
    ["B", "Run2018B-UL2018-v1"],
    ["C", "Run2018C-UL2018-v1"],
    ["D", "Run2018D-UL2018-v1"],
]

DataSets = ["MuonEG", "SingleMuon", "EGamma", "DoubleMuon"]

DataTrig = {
    "MuonEG": "Trigger_ElMu",
    "DoubleMuon": "!Trigger_ElMu && Trigger_dblMu",
    "SingleMuon": "!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu",
    "EGamma": "!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)",
}

#########################################
############ MC COMMON ##################
#########################################

METFilter_MC = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

# SFweight does not include btag weights
#mcCommonWeightNoMatch = "XSWeight*METFilter_MC*SFweight"
mcCommonWeight = "XSWeight * METFilter_MC * PromptGenLepMatch4l * SFweight"

###################################
########## EFT WEIGHTS ############
###################################

rwgt_sm = '(LHEReweightingWeight[0])'
rwgt_sm_lin_quad_cW = '(LHEReweightingWeight[1])'
rwgt_quad_cW = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[1] + LHEReweightingWeight[2] - 2*LHEReweightingWeight[0]))'
rwgt_sm_lin_quad_cHbox = '(LHEReweightingWeight[3])'
rwgt_quad_cHbox = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[3] + LHEReweightingWeight[4] - 2*LHEReweightingWeight[0]))'
rwgt_sm_lin_quad_cHDD = '(LHEReweightingWeight[5])'
rwgt_quad_cHDD = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[5] + LHEReweightingWeight[6] - 2*LHEReweightingWeight[0]))'
rwgt_sm_lin_quad_cHW = '(LHEReweightingWeight[7])'
rwgt_quad_cHW = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[7] + LHEReweightingWeight[8] - 2*LHEReweightingWeight[0]))'
rwgt_sm_lin_quad_cHWB = '(LHEReweightingWeight[9])'
rwgt_quad_cHWB = '(0.5*(1/1)*(1/1)*(LHEReweightingWeight[9] + LHEReweightingWeight[10] - 2*LHEReweightingWeight[0]))'



###########################################
#############  BACKGROUNDS  ###############
###########################################

###### VVV ######

samples['VVZ'] = { 'name' : nanoGetSampleFiles(mcDirectory, "WWZ")
                           +nanoGetSampleFiles(mcDirectory, "WZZ")
                           +nanoGetSampleFiles(mcDirectory, "ZZZ"),
                   'weight' : mcCommonWeight,
                   'FilesPerJob' : 5,
}

files = nanoGetSampleFiles(mcDirectory, "TTZToLLNuNu_M-10") 

###### ttZ ######

samples['ttZ'] = {
    'name': files,
    'weight' : mcCommonWeight,
    'FilesPerJob': 2,
}

###### ZZTo4l ####

files = nanoGetSampleFiles(mcDirectory, "ZZTo4L")

samples["ZZ4L"] = {
    "name": files,
    'weight' : mcCommonWeight+'*1.165',  # The NNLO/NLO k-factor, cited from https://arxiv.org/abs/1405.2219v1
    "FilesPerJob": 5,
}

###### ggZZ ######

mcDirectory = "/eos/user/m/mvannucc/nanoAOD/PostProc/ggZZ4l/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9"

samples['ggZZ'] = { 'name' : nanoGetSampleFiles2(mcDirectory, 'GluGluToZZTo4e')
                            +nanoGetSampleFiles2(mcDirectory, 'GluGluToZZTo4mu')
                            +nanoGetSampleFiles2(mcDirectory, 'GluGluToZZTo2e2mu'),
                    'weight' : mcCommonWeight+'*1.68', # The NLO/LO k-factor, cited from https://arxiv.org/abs/1509.06734v1
                    'FilesPerJob' : 5,
}

###### ZZTo4l QCD VBS ####

mcDirectory = "/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_QCD/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9"

files = nanoGetSampleFiles2(mcDirectory, "ZZJJTo4L_QCD")

samples["ZZJJTo4L_QCD"] = {
    "name": files,
    'weight' : mcCommonWeight,
    "FilesPerJob": 2,
}

###### EWK ZZ VBS #####

#mcDirectory = "/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EWK/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9"

#files = nanoGetSampleFiles2(mcDirectory, 'ZZJJTo4L_EWK')

#samples['ZZJJTo4L_EWK'] = { 
#        'name' : files,
#        'weight' : mcCommonWeight, 
#        'FilesPerJob' : 5,
#}


###########################################
################## DATA ###################
###########################################

samples["DATA"] = {
    "name": [],
    "weight": "LepWPCut*METFilter_DATA",
    "weights": [],
    "isData": ["all"],
    "FilesPerJob": 50,
}

for _, sd in DataRun:
    for pd in DataSets:
        datatag = pd + "_" + sd

        if (
            ("DoubleMuon" in pd and "Run2018B" in sd)
            or ("DoubleMuon" in pd and "Run2018D" in sd)
            or ("SingleMuon" in pd and "Run2018A" in sd)
            or ("SingleMuon" in pd and "Run2018B" in sd)
            or ("SingleMuon" in pd and "Run2018C" in sd)
        ):
            print("sd      = {}".format(sd))
            print("pd      = {}".format(pd))
            print("Old datatag = {}".format(datatag))
            datatag = datatag.replace("v1", "v2")
            print("New datatag = {}".format(datatag))

        files = nanoGetSampleFiles(dataDirectory, datatag)

        samples["DATA"]["name"].extend(files)
        addSampleWeight(samples, "DATA", datatag, DataTrig[pd])
        # samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))


files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['sm'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['sm_lin_quad_cW'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cW,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['quad_cW'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cW,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['sm_lin_quad_cHbox'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cHbox,
    'FilesPerJob': 4
}


files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['quad_cHbox'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cHbox,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['sm_lin_quad_cHDD'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cHDD,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['quad_cHDD'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cHDD,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['sm_lin_quad_cHW'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cHW,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['quad_cHW'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cHW,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['sm_lin_quad_cHWB'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_sm_lin_quad_cHWB,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles2('/eos/user/m/mvannucc/nanoAOD/PostProc/ZZJJTo4L_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9', 'ZZJJTo4L_EFT')
samples['quad_cHWB'] = {
    'name': files,
    'weight': mcCommonWeight+'*'+ rwgt_quad_cHWB,
    'FilesPerJob': 4
}

samples = {k:v for k,v in samples.items()} # SM + EFT
