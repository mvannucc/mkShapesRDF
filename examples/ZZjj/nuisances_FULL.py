# # merge cuts
# _mergedCuts = []
# for cut in list(cuts.keys()):
#     __cutExpr = ""
#     if type(cuts[cut]) == dict:
#         __cutExpr = cuts[cut]["expr"]
#         for cat in list(cuts[cut]["categories"].keys()):
#             _mergedCuts.append(cut + "_" + cat)
#     elif type(cuts[cut]) == str:
#         _mergedCuts.append(cut)
# 
# cuts2j = _mergedCuts

#from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''
nuisances = {}

##################
### LUMINOSITY ###
##################

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['ZZ'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['ZZ'])
}


nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['ZZ'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['ZZ'])
}

##########################
### TRIGGER EFFICIENCY ###
##########################

trig_syst = ['((TriggerEffWeight_4l_u)/(TriggerEffWeight_4l))*(TriggerEffWeight_4l>0.02) + (TriggerEffWeight_4l<=0.02)', '(TriggerEffWeight_4l_d)/(TriggerEffWeight_4l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

############################################
### Electron Efficiency and energy scale ###
############################################

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}

#nuisances['electronpt'] = {
#    'name': 'CMS_scale_e_2018',
#    'kind': 'suffix',
#    'type': 'shape',
#    'mapUp' : 'ElepTup',
#    'mapDown': 'ElepTdo',
#    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': makeMCDirectory('ElepTup_suffix'),
#    'folderDown': makeMCDirectory('ElepTdo_suffix'),
#    'AsLnN': '1'
#}

########################################
### Muon Efficiency and energy scale ###
########################################

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}

#nuisances['muonpt'] = {
#    'name': 'CMS_scale_m_2018',
#    'kind': 'suffix',
#    'type': 'shape',
#    'mapUp': 'MupTup',
#    'mapDown': 'MupTdo',
#    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': makeMCDirectory('MupTup_suffix'),
#    'folderDown': makeMCDirectory('MupTdo_suffix'),
#    'AsLnN': '1'
#}

########################
### Jet energy scale ###
########################

#jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']

#for js in jes_systs:
#  if 'Absolute' in js:
#    folderup = makeMCDirectory('JESAbsoluteup_suffix')
#    folderdo = makeMCDirectory('JESAbsolutedo_suffix')
#  elif 'BBEC1' in js:
#    folderup = makeMCDirectory('JESBBEC1up_suffix')
#    folderdo = makeMCDirectory('JESBBEC1do_suffix')
#  elif 'EC2' in js:
#    folderup = makeMCDirectory('JESEC2up_suffix')
#    folderdo = makeMCDirectory('JESEC2do_suffix')
#  elif 'HF' in js:
#    folderup = makeMCDirectory('JESHFup_suffix')
#    folderdo = makeMCDirectory('JESHFdo_suffix')
#  elif 'Relative' in js:
#    folderup = makeMCDirectory('JESRelativeup_suffix')
#    folderdo = makeMCDirectory('JESRelativedo_suffix')
#  elif 'FlavorQCD' in js:
#    folderup = makeMCDirectory('JESFlavorQCDup_suffix')
#    folderdo = makeMCDirectory('JESFlavorQCDdo_suffix')

#  nuisances[js] = {
#      'name': 'CMS_scale_'+js,
#      'kind': 'suffix',
#      'type': 'shape',
#      'mapUp': js+'up',
#      'mapDown': js+'do',
#      'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['VZ', 'Vg', 'VgS']),
#      'folderUp': folderup,
#      'folderDown': folderdo,
#      'AsLnN': '1'
#  }

##############
### Pileup ###
##############

pu_syst = '(puWeightUp/puWeight)', '(puWeightDown/puWeight)'

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
}
 
# # PDF
# pdf_variations = [
#     "LHEPdfWeight[%d]" % i for i in range(1, 101)
# ]  # Float_t LHE pdf variation weights (w_var / w_nominal) for LHA IDs  320901 - 321000
# nuisances["pdf_DY"] = {
#     "name": "CMS_hww_pdf_DY",
#     "kind": "weight_rms",
#     "type": "shape",
#     "AsLnN": "0",
#     "samples": {
#         "dyll": pdf_variations,
#     },
# }
# 
# variations = [
#     "LHEScaleWeight[0]",
#     "LHEScaleWeight[1]",
#     "LHEScaleWeight[3]",
#     "LHEScaleWeight[nLHEScaleWeight-4]",
#     "LHEScaleWeight[nLHEScaleWeight-2]",
#     "LHEScaleWeight[nLHEScaleWeight-1]",
# ]
# 
# nuisances["QCDscale_V"] = {
#     "name": "QCDscale_V",
#     "skipCMS": 1,
#     "kind": "weight_envelope",
#     "type": "shape",
#     "samples": {"dyll": variations},
#     "AsLnN": "0",
# }
# ##### MET energy scale
# 
# nuisances["met"] = {
#     "name": "CMS_scale_met_2018",
#     "kind": "suffix",
#     "type": "shape",
#     "mapUp": "METup",
#     "mapDown": "METdo",
#     "samples": dict((skey, ["1", "1"]) for skey in mc),
#     "folderUp": makeMCDirectory("METup_suffix"),
#     "folderDown": makeMCDirectory("METdo_suffix"),
#     "AsLnN": "1",
# }
# 

autoStats = True
if autoStats:
    ## Use the following if you want to apply the automatic combine MC stat nuisances.
    nuisances["stat"] = {
        "type": "auto",
        "maxPoiss": "10",
        "includeSignal": "0",
        #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
        #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
        "samples": {},
    }
