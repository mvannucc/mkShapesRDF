#ifndef MLL2_H
#define MLL2_H

#include <vector>
#include "TLorentzVector.h"
#include "ROOT/RVec.hxx"

double mll2(
    int nLepton,		
    ROOT::RVec<float> Lepton_pt,
    ROOT::RVec<float> Lepton_eta,
    ROOT::RVec<float> Lepton_phi,
    ROOT::RVec<int> Lepton_pdgId
) {
    const double muon_mass = 0.1056583745;         // GeV
    const double electron_mass = 0.0005109989461;  // GeV
    double result_mll2 = -1.0;
    int foundPairs = 0;
    
    if (nLepton == 4){
        for (unsigned int i = 0; i < nLepton; ++i) {
            int charge1 = (Lepton_pdgId[i] > 0) ? -1 : 1;
            double mass1 = (abs(Lepton_pdgId[i]) == 13) ? muon_mass : electron_mass;

            for (unsigned int j = i + 1; j < nLepton; ++j) {
                int charge2 = (Lepton_pdgId[j] > 0) ? -1 : 1;
            	double mass2 = (abs(Lepton_pdgId[j]) == 13) ? muon_mass : electron_mass;

            	if (abs(Lepton_pdgId[i]) == abs(Lepton_pdgId[j]) && (charge1 * charge2 == -1)) {
                    TLorentzVector l1, l2;

                    l1.SetPtEtaPhiM(Lepton_pt[i], Lepton_eta[i], Lepton_phi[i], mass1);
                    l2.SetPtEtaPhiM(Lepton_pt[j], Lepton_eta[j], Lepton_phi[j], mass2);

                    if (foundPairs == 1) {
                        result_mll2 = (l1 + l2).M();
                        return result_mll2;
                    }
                    ++foundPairs;
                }
            }
        }
    } //end if nLepton
    return result_mll2;
}

#endif

