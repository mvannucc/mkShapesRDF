#ifndef M4L_H
#define M4L_H

#include <vector>
#include "TLorentzVector.h"
#include "ROOT/RVec.hxx"

double m4l(
    int nLepton,
    ROOT::RVec<float> Lepton_pt,
    ROOT::RVec<float> Lepton_eta,
    ROOT::RVec<float> Lepton_phi,
    ROOT::RVec<int> Lepton_pdgId
) {
    const double muon_mass = 0.1056583745;         // GeV
    const double electron_mass = 0.0005109989461;  // GeV
    double result_m4l = -1.0;

    if (nLepton == 4) {
        std::vector<TLorentzVector> selectedLeptons;

        for (unsigned int i = 0; i < nLepton; ++i) {
            double mass = (abs(Lepton_pdgId[i]) == 13) ? muon_mass : electron_mass;
            TLorentzVector lepton;
            lepton.SetPtEtaPhiM(Lepton_pt[i], Lepton_eta[i], Lepton_phi[i], mass);
            selectedLeptons.push_back(lepton);
        }

        TLorentzVector totalVec = selectedLeptons[0] + selectedLeptons[1] + selectedLeptons[2] + selectedLeptons[3];
        result_m4l = totalVec.M();
    }

    return result_m4l;
}

#endif

