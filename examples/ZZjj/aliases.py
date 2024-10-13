import os
import copy
import inspect


#configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = '/afs/cern.ch/user/m/mvannucc/workspace/mkShapesRDF/examples/ZZjj'

aliases = {}
aliases = OrderedDict()

#mc     = [skey for skey in samples if skey not in ('Fake', 'DATA', 'Dyemb')]
#mc_emb = [skey for skey in samples if skey not in ('Fake', 'DATA')]

#mc        = [skey for skey in samples if skey not in ('DATA', 'Fake_lep') and skey not in mcEFT]
mc     = [skey for skey in samples if skey not in ('DATA', 'Fake_lep')]

eleWP = 'mvaFall17V2Iso_WP90'
muWP  = 'cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut4l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

aliases['LepWPSF'] = {
    'expr': 'LepSF4l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass < 0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4l',
    'samples': ['Fake_lep']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
            'expr': 'Alt(Lepton_promptgenmatched, 0, 0) * Alt(Lepton_promptgenmatched, 1, 0)',
            'samples': mc
}

aliases['PromptGenLepMatch4l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)*Alt(Lepton_promptgenmatched,2,0)*Alt(Lepton_promptgenmatched,3,0)',
    'samples': mc
}

aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}


# # my macro
# print('\n\n\n')
# print('Configs:\n\n\n')
# configurations = os.path.abspath('.') + '/' 
# print(configurations)
# print('\n\n\n')
# ##### DY Z pT reweighting
# aliases['nCleanGenJet'] = {
#     'linesToAdd': ['#include "%s/ngenjet.cc"' % configuration],
#     'samples': mc
# }


# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt(CleanJet_pt, 0, 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt(CleanJet_pt, 0, 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt(CleanJet_pt, 1, 0) > 30.'
}

aliases['bVeto'] = {
    'expr': 'Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepFlavB, CleanJet_jetIdx) > 0.0490) == 0'
}
aliases['bReq'] = { 
    'expr': 'Sum(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepFlavB, CleanJet_jetIdx) > 0.0490) >= 1'
}

# CR definition

aliases['topcr'] = {
    'expr': 'mll>50 && ((zeroJet && !bVeto) || bReq)'
}


aliases['lowZ'] = {
    'expr':  '0.5*abs((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1])) < 1'        
}

aliases['highZ'] = {
    'expr':  '0.5*abs((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1])) >= 1'
}


# SF
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepjet_shape, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepjet_shape, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
    'samples': mc
}

for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:

    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_deepjet_shape', 'btagSF_deepjet_shape_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_deepjet_shape', 'btagSF_deepjet_shape_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }

aliases['Jet_PUIDSF'] = { 
          'expr' : 'TMath::Exp(Sum(LogVec(Jet_PUIDSF_loose)))',
          'samples': mc
}
# aliases['Jet_PUIDSF_up'] = {
#  'expr' : 'TMath::Exp(Sum(LogVec(Jet_PUIDSF_loose_up)))',
#  'samples': mc
# }
# aliases['Jet_PUIDSF_down'] = {
#  'expr' : 'TMath::Exp(Sum(LogVec(Jet_PUIDSF_loose_down)))',
#  'samples': mc
# }



aliases['Zepp_l1'] = {
    'expr': 'Lepton_eta[0] - (CleanJet_eta[0] + CleanJet_eta[1])/2'
}

aliases['Zepp_l2'] = {
    'expr': 'Lepton_eta[1] - (CleanJet_eta[0] + CleanJet_eta[1])/2'
}

aliases['Zepp_ll'] = {
    'expr': '0.5*abs((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1]))'
}

aliases['Rpt'] = {
    'expr': 'Lepton_pt[0]*Lepton_pt[1]/(CleanJet_pt[0]*CleanJet_pt[1])'
}

# data/MC scale factors

aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight4l', 'LepWPCut', 'LepWPSF','Jet_PUIDSF', 'btagSF']),
    'samples': mc
}
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}

# Two leading jets matched to gen-level jets with pT > 25 GeV 
aliases['hardJets'] = {
    'expr':  'Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 25 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 25', 
    'samples': ['dyll']
}

aliases['PUJets'] = {
    'expr':  '!(Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 25 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 25)',
    'samples': ['dyll']
}

# Number of hard (= gen-matched) jets
aliases['nHardJets'] = {
    'expr':  'Sum(Jet_genJetIdx[CleanJet_jetIdx] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx]] > 25)',
    'samples': ['dyll']
}

aliases['lhe_mjj'] = {
    'expr': 'TMath::Sqrt(2. * LHEPart_pt[4] * LHEPart_pt[5] * (TMath::CosH(LHEPart_eta[4] - LHEPart_eta[5]) - TMath::Cos(LHEPart_phi[4] - LHEPart_phi[5])))',
    'samples': ['Zjj']
}

##################
# custom aliases #
##################

aliases['mll1'] = {
  'linesToAdd': ['#include "%s/mll1.cc"' % configurations],  
  'class': 'mll1',
  'args': 'nLepton, Lepton_pt, Lepton_eta, Lepton_phi, Lepton_pdgId',
}

aliases['mll2'] = {
  'linesToAdd': ['#include "%s/mll2.cc"' % configurations],
  'class': 'mll2',
  'args': 'nLepton, Lepton_pt, Lepton_eta, Lepton_phi, Lepton_pdgId',
}

aliases['m4l'] = {
  'linesToAdd': ['#include "%s/m4l.cc"' % configurations],
  'class': 'm4l',
  'args': 'nLepton, Lepton_pt, Lepton_eta, Lepton_phi, Lepton_pdgId',
}

aliases['Detajj'] = {
        'expr': 'abs(Alt(CleanJet_eta, 0, -1000) - Alt(CleanJet_eta, 1, 1000))',
}


