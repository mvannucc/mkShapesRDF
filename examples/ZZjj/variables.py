# variables

variables = {}

variables["m4l"] = {
    "name": "m4l",  
    "range": (25, 180, 1400), 
    "xaxis": "M_{4l} [GeV]",  
    "fold": 0,
}

variables["mjj"] = {
    "name": "mjj",
    "range": (30, 100, 1300),
    "xaxis": "M_{jj}",
    "fold": 0,
}

variables["delta_eta_jets"] = {
    "name": "(Sum(CleanJet_pt>30)>1)*(Alt(CleanJet_eta, 0, 0) - Alt(CleanJet_eta, 1, 0)) - (Sum(CleanJet_pt>30)<=1)*99",
    "range": (20, 0, 8),
    "xaxis": "#Delta#eta_{jj}",
    "fold": 0,
}


variables["jet_pt"] = {
    "name": "(Sum(CleanJet_pt>30)>1)*(Alt(CleanJet_pt, 1, 0)) + (Sum(CleanJet_pt>30)>0)*(Alt(CleanJet_pt, 0, 0)) - (Sum(CleanJet_pt>30)==0)*99",
    "range": (30, 0, 400),
    "xaxis": "p_{T,j}",
    "fold": 0,
}

variables["jet_eta"] = {
    "name": "(Sum(CleanJet_pt>30)>1)*(Alt(CleanJet_eta, 1, 0)) + (Sum(CleanJet_pt>30)>0)*(Alt(CleanJet_eta, 0, 0)) - (Sum(CleanJet_pt>30)==0)*99",
    "range": (40, -5, 5),
    "xaxis": "#eta_{j}",
    "fold": 0,
}

