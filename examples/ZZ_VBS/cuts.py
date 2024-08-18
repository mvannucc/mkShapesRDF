# cuts
cuts = {}

preselections = 'multiJet && abs(Alt(CleanJet_eta,0,-9999))<4.7 && abs(Alt(CleanJet_eta,1,-9999))<4.7 && mjj > 100 && \
        Alt(Lepton_pt,0,0)>20 && Alt(Lepton_pt,1,0)>10 && Alt(Lepton_pt,2,0)>5 && Alt(Lepton_pt,3,0)>5 && \
        abs(Alt(Lepton_eta,0,0))<2.5 && abs(Alt(Lepton_eta,1,0))<2.5 && abs(Alt(Lepton_eta,2,0))<2.5 && abs(Alt(Lepton_eta,3,0))<2.5 && \
        ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13))'

triple_charge_zz = '((abs(Alt(Lepton_pdgId,0,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[0],0)==2) || abs(Alt(Lepton_pdgId,0,0))==13) && \
                    ((abs(Alt(Lepton_pdgId,1,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[1],0)==2) || abs(Alt(Lepton_pdgId,1,0))==13) && \
                    ((abs(Alt(Lepton_pdgId,2,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[2],0)==2) || abs(Alt(Lepton_pdgId,2,0))==13) && \
                    ((abs(Alt(Lepton_pdgId,3,0))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[3],0)==2) || abs(Alt(Lepton_pdgId,3,0))==13)'
Z_tag = 'mll > 60 && mll < 120'
#ZZ_tag = 'm4l > 180'

deltaR = 'dR_l1l2'

cuts['ZZ'] = Z_tag+'&&'+deltaR

#cuts['Z']  = {
#   'expr' : 'true',
#   'categories' : {
#      'ee_inclusive' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11)',
#      'mm_inclusive' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13)',
#   }
#}

#cuts['Zee']  = {
#   'expr' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11)',
#   'categories' : {
#      '0j' : 'zeroJet',
#      '1j' : 'oneJet && Alt(CleanJet_pt,1,0)<30',
#      '2j' : 'multiJet',
#   }
#}

#cuts['Zmm']  = {
#   'expr' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13)',
#   'categories' : {
#      '0j' : 'zeroJet',
#      '1j' : 'oneJet && Alt(CleanJet_pt,1,0)<30',
#      '2j' : 'multiJet',
#   }
#}



