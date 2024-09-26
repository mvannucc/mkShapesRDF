# cuts
cuts = {}

preselections = 'multiJet && abs(Alt(CleanJet_eta,0,-9999))<4.7 && abs(Alt(CleanJet_eta,1,-9999))<4.7 && \
                 Alt(Lepton_pt,0,0)>20 && Alt(Lepton_pt,1,0)>10 && Alt(Lepton_pt,2,0)>5 && Alt(Lepton_pt,3,0)>5 && \
                 abs(Alt(Lepton_eta,0,0))<2.5 && abs(Alt(Lepton_eta,1,0))<2.5 && abs(Alt(Lepton_eta,2,0))<2.5 && abs(Alt(Lepton_eta,3,0))<2.5'

#lepton_id = '((abs(Alt(Lepton_pdgId,0,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[0],0)==2) || abs(Alt(Lepton_pdgId,0,0))==13) && \
#             ((abs(Alt(Lepton_pdgId,1,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[1],0)==2) || abs(Alt(Lepton_pdgId,1,0))==13) && \
#             ((abs(Alt(Lepton_pdgId,2,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[2],0)==2) || abs(Alt(Lepton_pdgId,2,0))==13) && \
#             ((abs(Alt(Lepton_pdgId,3,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[3],0)==2) || abs(Alt(Lepton_pdgId,3,0))==13)'

Z_tag = 'mll > 60 && mll < 120'
ZZ_tag = 'm4l > 180'

lep = 'nLepton>=2'

#new_mll = 'mll1 > 0 && mll2 > 0'

#deltaR = 'dR_l1j1 > 0.4 && dR_l1j2 > 0.4 && dR_l2j1 > 0.4 && dR_l2j2 > 0.4 && \
#          dR_l3j1 > 0.4 && dR_l3j2 > 0.4 && dR_l4j1 > 0.4 && dR_l4j2 > 0.4'

baseline = 'mjj > 100'
VBS_loose = 'Detajj > 2.4 && mjj > 400'
VBS_tight = 'Detajj > 2.4 && mjj > 1000'

cuts['ZZ'] = {
    'expr': lep,#Z_tag,#+'&&'+ZZ_tag,#+'&&'+deltaR,
    'categories': {
        'Baseline': baseline,
        #'VBS_loose': VBS_loose,
        #'VBS_tight': VBS_tight,
    }
}









