# variables

variables = {}

variables["pt_all"] = {
    "name": "Alt(Lepton_pt, 0, 0) + Alt(Lepton_pt, 1, 0) + Alt(Lepton_pt, 2, 0) + Alt(Lepton_pt, 3, 0)",
    "range": (20, 160, 1000),
    "xaxis": "M_{4l} [GeV]",
    "fold": 0,
}

variables["pt_jet1"] = {
    "name": "Alt(CleanJet_pt, 0, 0)",
    "range": (20, 160, 2000),
    "xaxis": "p_{T,j1} [GeV]",
    "fold": 0,
}

variables["pt_jet2"] = {
    "name": "Alt(CleanJet_pt, 1, 0)",
    "range": (20, 160, 2000),
    "xaxis": "p_{T,j2} [GeV]",
    "fold": 0,
}

variables["m4l"] = {
    "name": "mllll_zh4l",
    "range": (20, 160, 1000),
    "xaxis": "M_{4l} [GeV]",
    "fold": 0,
}

variables["delta_eta_jets"] = {
    "name": "Detajj",
    "range": (20, 0, 8),
    "xaxis": "#Delta#eta_{jj}",
    "fold": 0,
}

variables["mjj"] = {
    "name": "mjj",
    "range": (20, 0, 1500),
    "xaxis": "M_{jj}",
    "fold": 0,
}

variables["Zepp_l1"] = {
    "name": "Zepp_l1",
    "range": (10, -5, 5),
    "xaxis": "Zepp_l1",
    "fold": 0,
}

variables["Zepp_l2"] = {
    "name": "Zepp_l2",
    "range": (10, -5, 5),
    "xaxis": "Zepp_l2",
    "fold": 0,
}

variables["deltaR_ZZ"] = {
    "name": "deltaR_ZZ",
    "range": (10, -4, 4),
    "xaxis": "deltaR_ZZ",
    "fold": 0,
}

variables["pt1"] = {
    "name": "Alt(Lepton_pt, 0, 0)",
    "range": (30, 0., 350),
    "xaxis": "lept1_p_{T} [GeV]",
    "fold": 0,
}

variables["pt2"] = {
    "name": "Alt(Lepton_pt, 1, 0)",
    "range": (30, 0., 350),
    "xaxis": "lept2_p_{T} [GeV]",
    "fold": 0,
}

variables["pt3"] = {
    "name": "Alt(Lepton_pt, 2, 0)",
    "range": (30, 0., 250),
    "xaxis": "lept3_p_{T} [GeV]",
    "fold": 0,
}

variables["pt4"] = {
    "name": "Alt(Lepton_pt, 3, 0)",
    "range": (30, 0., 250),
    "xaxis": "lept4_p_{T} [GeV]",
    "fold": 0,
}

variables["pt_sum_pos"] = {
    "name": "pt_sum_pos",
    "range": (30, 0., 550),
    "xaxis": "p_{T,+} [GeV]",
    "fold": 0,
}

