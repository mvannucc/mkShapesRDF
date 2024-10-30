# cuts
cuts = {}

#preselections = 'nLepton >= 4 && \
#                 Alt(Lepton_pt,0,0) > 20 && \
#                 Alt(Lepton_pt,1,0) > 10 && \
#                 Alt(Lepton_pt,2,0) > 5 && \
#                 Alt(Lepton_pt,3,0) > 5 && \
#                 abs(Alt(Lepton_eta,0,0)) < 2.5 && \
#                 abs(Alt(Lepton_eta,1,0)) < 2.5 && \
#                 abs(Alt(Lepton_eta,2,0)) < 2.5 && \
#                 abs(Alt(Lepton_eta,3,0)) < 2.5'

preselections = '\
                 Alt(Lepton_pt,0,0) > 20 && \
                 Alt(Lepton_pt,1,0) > 10 && \
                 abs(Alt(Lepton_eta,0,0)) < 2.5 && \
                 abs(Alt(Lepton_eta,1,0)) < 2.5'

tagging_jets = 'nJet >= 2 && \
                Alt(CleanJet_pt,0,-9999) > 30 && \
                Alt(CleanJet_pt,1,-9999) > 30 && \
                abs(Alt(CleanJet_eta,0,9999)) < 4.7 && \
                abs(Alt(CleanJet_eta,1,9999)) < 4.7'

jet = 'Alt(CleanJet_pt,0,-9999) > 30 && \
       Alt(CleanJet_pt,1,-9999) > 30'
       
Z0_tag = 'z0Mass_zh4l > 60 && z0Mass_zh4l < 120'
Z1_tag = 'z1Mass_zh4l > 60 && z1Mass_zh4l < 120'

m4l = 'mllll_zh4l > 180'

baseline = 'mjj > 100'

VBS_loose = 'Detajj > 2.4 && mjj > 400'
VBS_tight = 'Detajj > 2.4 && mjj > 1000'

cuts['ZZ'] = {
    'expr': Z0_tag + '&&' + Z1_tag,# + '&&' + m4l,
    'categories': {
        'Baseline': baseline + '&&' + jet + '&&' + m4l,
        #'Full': baseline + '&&' + tagging_jets + '&&' + m4l,
        #'VBS_loose': VBS_loose,
        #'VBS_tight': VBS_tight,
    }
}









