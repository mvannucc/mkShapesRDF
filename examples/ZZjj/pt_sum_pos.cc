#ifndef SUMPT_POSITIVE_H
#define SUMPT_POSITIVE_H

#include <vector>
#include <algorithm>
#include "TLorentzVector.h"
#include "ROOT/RVec.hxx"

double pt_sum_pos(
    int nLepton,
    ROOT::RVec<float> Lepton_pt,
    ROOT::RVec<float> Lepton_eta,
    ROOT::RVec<float> Lepton_phi,
    ROOT::RVec<int> Lepton_pdgId
) {
    double result_sumPt = 0.0;

    if (nLepton < 2) {
        return result_sumPt; // Not enough leptons
    }

    // Create a vector of indices to sort leptons by pt
    std::vector<int> indices(nLepton);
    std::iota(indices.begin(), indices.end(), 0);

    // Sort indices based on Lepton_pt in descending order
    std::sort(indices.begin(), indices.end(), [&](int i, int j) {
        return Lepton_pt[i] > Lepton_pt[j];
    });

    // Take the first 4 leptons (if there are at least 4)
    int maxLeptons = std::min(4, nLepton);
    std::vector<int> topLeptons(indices.begin(), indices.begin() + maxLeptons);

    // Filter out leptons with positive charge
    std::vector<int> positiveLeptons;
    for (int idx : topLeptons) {
        if (Lepton_pdgId[idx] > 0) { // Positive charge
            positiveLeptons.push_back(idx);
        }
        if (positiveLeptons.size() == 2) {
            break; // Only take the first 2 positive charge leptons
        }
    }

    // Calculate the sum of pt for the selected leptons
    for (int idx : positiveLeptons) {
        result_sumPt += Lepton_pt[idx];
    }

    return result_sumPt;
}

#endif
