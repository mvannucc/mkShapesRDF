# cuts
cuts = {}

preselections = 'nJet >=2 && \
                 Alt(CleanJet_pt,0,-9999) > 30 && \
                 Alt(CleanJet_pt,1,-9999) > 30 && \
                 abs(Alt(CleanJet_eta,0,-9999)) < 4.7 && \
                 abs(Alt(CleanJet_eta,1,-9999)) < 4.7 && \
                 nLepton == 4 && \
                 Alt(Lepton_pt,0,0) > 20 && \
                 Alt(Lepton_pt,1,0) > 10 && \
                 Alt(Lepton_pt,2,0) > 5 && \
                 Alt(Lepton_pt,3,0) > 5 && \
                 abs(Alt(Lepton_eta,0,0)) < 2.5 && \
                 abs(Alt(Lepton_eta,1,0)) < 2.5 && \
                 abs(Alt(Lepton_eta,2,0)) < 2.5 && \
                 abs(Alt(Lepton_eta,3,0)) < 2.5'

Z1_tag = 'mll1 > 60 && mll1 < 120'
Z2_tag = 'mll2 > 60 && mll2 < 120'

ZZ_tag = 'm4l > 180'

#deltaR = 'dR_l1j1 > 0.4 && dR_l1j2 > 0.4 && dR_l2j1 > 0.4 && dR_l2j2 > 0.4 && \
#          dR_l3j1 > 0.4 && dR_l3j2 > 0.4 && dR_l4j1 > 0.4 && dR_l4j2 > 0.4'

baseline = 'mjj > 100'
VBS_loose = 'Detajj > 2.4 && mjj > 400'
VBS_tight = 'Detajj > 2.4 && mjj > 1000'

cuts['ZZ'] = {
    'expr': Z1_tag + '&&' + Z2_tag + '&&' + ZZ_tag,
    'categories': {
        'Baseline': baseline,
        #'VBS_loose': VBS_loose,
        #'VBS_tight': VBS_tight,
    }
}









