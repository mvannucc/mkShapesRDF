# variables

variables = {}

#variables["m4l"] = {
#    "name": "mllll_zh4l",  
#    "range": (25, 160, 1400), 
#    "xaxis": "M_{4l} [GeV]",  
#    "fold": 0,
#}

variables["mjj"] = {
    "name": "mjj",
    "range": (30, 100, 1300),
    "xaxis": "M_{jj}",
    "fold": 0,
}

#variables["delta_eta_jets"] = {
#    "name": "(Sum(CleanJet_pt>30)>1)*(Alt(CleanJet_eta, 0, 0) - Alt(CleanJet_eta, 1, 0)) - (Sum(CleanJet_pt>30)<=1)*99",
#    "range": (20, 0, 8),
#    "xaxis": "#Delta#eta_{jj}",
#    "fold": 0,
#}


variables["jet_pt"] = {
    "name": "(Sum(CleanJet_pt>30)>1)*(Alt(CleanJet_pt, 1, 0)) + (Sum(CleanJet_pt>30)>0)*(Alt(CleanJet_pt, 0, 0)) - (Sum(CleanJet_pt>30)==0)*99",
    "range": (30, 0, 400),
    "xaxis": "p_{T,j}",
    "fold": 0,
}

#variables["jet_eta"] = {
#    "name": "(Sum(CleanJet_pt>30)>1)*(Alt(CleanJet_eta, 1, 0)) + (Sum(CleanJet_pt>30)>0)*(Alt(CleanJet_eta, 0, 0)) - (Sum(CleanJet_pt>30)==0)*99",
#    "range": (40, -5, 5),
#    "xaxis": "#eta_{j}",
#    "fold": 0,
#}

variables["nlep"] = {
    "name": "nLepton",
    "range": (8, 0, 8),
    "xaxis": "nlep",
    "fold": 0,
}

variables["njet"] = {
    "name": "nJet",
    "range": (8, 0, 8),
    "xaxis": "njet",
    "fold": 0,
}

variables["pt1"] = {
    "name": "Alt(Lepton_pt, 0, 0)",
    "range": (30, 0., 250),
    "xaxis": "lept1_p_{T} [GeV]",
    "fold": 0,
}

variables["pt2"] = {
    "name": "Alt(Lepton_pt, 1, 0)",
    "range": (30, 0., 250),
    "xaxis": "lept2_p_{T} [GeV]",
    "fold": 0,
}

variables['pt4']  = {   
        'name': 'Alt(Lepton_pt, 3, 0)',            #   variable name
        'range' : (30,0.,200),    #   variable range
        'xaxis' : 'lept4_p_{T} [GeV]',  #   x axis name
        'fold' : 0
}

#variables['Z0mass']  = {
#        'name': 'z0Mass_zh4l',            #   variable name
#        'range' : (30,50,130),    #   variable range
#        'xaxis' : 'M_{Z_0} [GeV]',  #   x axis name
#        'fold' : 0
#}

#variables['Z1mass']  = {
#        'name': 'z1Mass_zh4l',            #   variable name
#        'range' : (30,50,130),    #   variable range
#        'xaxis' : 'M_{Z_1} [GeV]',  #   x axis name
#        'fold' : 0
#}



