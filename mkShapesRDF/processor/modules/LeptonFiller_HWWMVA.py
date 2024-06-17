from mkShapesRDF.processor.framework.module import Module
import os
import ROOT
import correctionlib
correctionlib.register_pyroot_binding()

class LeptonFiller_HWWMVA(Module):
    def __init__(self, script_path="processor/data/HWW-Run3-LeptonMVA/"):
        super().__init__("LeptonFiller_HWWMVA")

        if "processor" in os.path.dirname(os.path.dirname(__file__)):
            self.script_path = (
                os.path.dirname(os.path.dirname(__file__)).split("processor")[0]
                + script_path
            )
        else:
            self.script_path = script_path

        
    def runModule(self, df, values):

        if not hasattr(ROOT, "getJetPtRatio"):
            ROOT.gInterpreter.Declare(
                """
                ROOT::RVecF getJetPtRatio(ROOT::RVecF Muon_jetRelIso){
                    ROOT::RVecF result(Muon_jetRelIso.size(), 1.5);
                    float tmp_value = 0.0;
                    for (int i=0; i<Muon_jetRelIso.size(); i++){
                        tmp_value = 1.0 / (1.0 + Muon_jetRelIso[i]);
                        if (tmp_value<1.5){
                            result[i] = tmp_value;
                        }
                    }
                    return result;
                }
                """
            )

        ### Use Python-API to evaluate XGBoost model in ROOT RDF
        ROOT.gInterpreter.Declare(
            """
            #include <vector>
            #include <iostream>
            #include <TMath.h>
            #include <math.h>
            
            #include "TFile.h"
            #include "TTree.h"
            #include "TString.h"
            #include "TSystem.h"
            #include "TROOT.h"
            
            #include <boost/python.hpp>
            #include <boost/python/numpy.hpp>
            
            #include "ROOT/RVec.hxx"
            
            #include <Python.h>
            
            using namespace ROOT;
            using namespace ROOT::VecOps;
            
            std::vector<RVecF> evaluate_mva(
                RVecF Muon_pt,
                RVecF Muon_eta,
                RVecF Muon_pfRelIso03_all,
                RVecF Muon_miniPFRelIso_chg,
                RVecF Muon_miniRelIsoNeutral,
                RVecF Muon_jetNDauCharged,
                RVecF Muon_jetPtRelv2,
                RVecF Muon_jetPtRatio,
                RVecF Muon_jetBTagDeepFlavB,
                RVecF Muon_sip3d,
                RVecF Muon_log_dxy,
                RVecF Muon_log_dz,
                RVecF Muon_segmentComp,
                RVecF Muon_nStations,
                RVecF Muon_nTrackerLayers,
                RVecF Muon_highPurity,
                RVecF Muon_bsConstrainedChi2,
                RVecF Muon_tkRelIso,
                RVecF Electron_pt,
                RVecF Electron_eta,
                RVecF Electron_pfRelIso03_all,
                RVecF Electron_miniPFRelIso_chg,
                RVecF Electron_miniRelIsoNeutral,
                RVecF Electron_jetNDauCharged,
                RVecF Electron_jetPtRelv2,
                RVecF Electron_jetPtRatio,
                RVecF Electron_jetBTagDeepFlavB,
                RVecF Electron_sip3d,
                RVecF Electron_log_dxy,
                RVecF Electron_log_dz,
                RVecF Electron_mvaIso,
                RVecF Electron_lostHits,
                RVecF Electron_scEtOverPt,
                RVecF Electron_r9,
                RVecF Electron_sieie,
                RVecF Electron_hoe,
                RVecF Electron_eInvMinusPInv,
                RVecF Electron_dr03TkSumPt
            ){
                
                std::vector<RVecF> results;
    
                RVecF result_muon(Muon_pt.size(), -1.0);
                RVecF result_electron(Electron_pt.size(), -1.0);
    
                PyObject* sysPath = PySys_GetObject("path");"""+f"""
                PyList_Append(sysPath, PyUnicode_DecodeFSDefault("{self.script_path}"));"""+"""
                PyObject* pModule_electron = PyImport_ImportModule("Evaluate_electrons");
                PyObject* pModule_muon = PyImport_ImportModule("Evaluate_muons");
    
                if (pModule_muon != NULL && pModule_electron != NULL) {
        
                    PyObject* pFunction_muon = PyObject_GetAttrString(pModule_muon, "load_muon_hwwmva");
                    PyObject* pFunction_electron = PyObject_GetAttrString(pModule_electron, "load_electron_hwwmva");
        
                    if (pFunction_muon != NULL && pFunction_electron != NULL) {
            
                        /// ---------------------------
                        /// Muons
                        /// ---------------------------
                        
                        for (int i=0; i<Muon_pt.size(); i++){
                                
                            std::vector<float> input_muon;
                            
                            input_muon.push_back(Muon_pt[i]);
                            input_muon.push_back(Muon_eta[i]);
                            input_muon.push_back(Muon_pfRelIso03_all[i]);
                            input_muon.push_back(Muon_miniPFRelIso_chg[i]);
                            input_muon.push_back(Muon_miniRelIsoNeutral[i]);
                            input_muon.push_back(Muon_jetNDauCharged[i]);
                            input_muon.push_back(Muon_jetPtRelv2[i]);
                            input_muon.push_back(Muon_jetPtRatio[i]);
                            input_muon.push_back(Muon_jetBTagDeepFlavB[i]);
                            input_muon.push_back(Muon_sip3d[i]);
                            input_muon.push_back(Muon_log_dxy[i]);
                            input_muon.push_back(Muon_log_dz[i]);
                            input_muon.push_back(Muon_segmentComp[i]);
                            input_muon.push_back(Muon_nStations[i]);
                            input_muon.push_back(Muon_nTrackerLayers[i]);
                            input_muon.push_back(Muon_highPurity[i]);
                            input_muon.push_back(Muon_bsConstrainedChi2[i]);
                            input_muon.push_back(Muon_tkRelIso[i]);
                
                            PyObject* pList_muon = PyList_New(18);
                            for (int j = 0; j < 18; ++j) {
                                PyList_SetItem(pList_muon, j, PyFloat_FromDouble((double)input_muon[j]));
                            }
                            PyObject* pArgs_muon = PyTuple_Pack(1, pList_muon);
                
                            if (pArgs_muon != NULL){
                                
                                PyObject* pValue_muon = PyObject_CallObject(pFunction_muon, pArgs_muon);
                                
                                if (pValue_muon != NULL){
                                    if (PyList_Check(pValue_muon)) {
                                        Py_ssize_t listSize_muon = PyList_Size(pValue_muon);
                                        
                                        for (Py_ssize_t k = 0; k < listSize_muon; k++) {
                                            PyObject* listItem_muon = PyList_GetItem(pValue_muon, k);
                                            
                                            result_muon[i] = (float)PyFloat_AsDouble(listItem_muon);
                                            
                                        }
                                    } else {
                                        PyErr_Print();
                                    }
                                }                                
                            }                
                        }
            
                        /// ---------------------------
                        /// Electrons
                        /// ---------------------------
            
            
                        for (int i=0; i<Electron_pt.size(); i++){
                
                            std::vector<float> input_electron;
                
                            input_electron.push_back(Electron_pt[i]);
                            input_electron.push_back(Electron_eta[i]);
                            input_electron.push_back(Electron_pfRelIso03_all[i]);
                            input_electron.push_back(Electron_miniPFRelIso_chg[i]);
                            input_electron.push_back(Electron_miniRelIsoNeutral[i]);
                            input_electron.push_back(Electron_jetNDauCharged[i]);
                            input_electron.push_back(Electron_jetPtRelv2[i]);
                            input_electron.push_back(Electron_jetPtRatio[i]);
                            input_electron.push_back(Electron_jetBTagDeepFlavB[i]);
                            input_electron.push_back(Electron_sip3d[i]);
                            input_electron.push_back(Electron_log_dxy[i]);
                            input_electron.push_back(Electron_log_dz[i]);
                            input_electron.push_back(Electron_mvaIso[i]);
                            input_electron.push_back(Electron_lostHits[i]);
                            input_electron.push_back(Electron_scEtOverPt[i]);
                            input_electron.push_back(Electron_r9[i]);
                            input_electron.push_back(Electron_sieie[i]);
                            input_electron.push_back(Electron_hoe[i]);
                            input_electron.push_back(Electron_eInvMinusPInv[i]);
                            input_electron.push_back(Electron_dr03TkSumPt[i]);
                                
                            PyObject* pList_electron = PyList_New(20);
                            for (int j = 0; j < 20; ++j) {
                                PyList_SetItem(pList_electron, j, PyFloat_FromDouble((double)input_electron[j]));
                            }
                            PyObject* pArgs_electron = PyTuple_Pack(1, pList_electron);
                
                            if (pArgs_electron != NULL){
                    
                                PyObject* pValue_electron = PyObject_CallObject(pFunction_electron, pArgs_electron);
                                    
                                if (pValue_electron != NULL){
                                    if (PyList_Check(pValue_electron)) {
                                        Py_ssize_t listSize_electron = PyList_Size(pValue_electron);
                                        
                                        for (Py_ssize_t k = 0; k < listSize_electron; k++) {
                                            PyObject* listItem_electron = PyList_GetItem(pValue_electron, k);
                                            result_electron[i] = (float)PyFloat_AsDouble(listItem_electron);
                                        }
                                    } else {
                                        PyErr_Print();
                                    }
                                }                                    
                            }                                
                        }           
                    }else {
                        PyErr_Print();
                    }        
                }else {
                    PyErr_Print();
                }
                results.push_back(result_muon);
                results.push_back(result_electron);
                return results;       
            }
            """
        )

        df = df.Define("Muon_miniRelIsoNeutral", "Muon_miniPFRelIso_all - Muon_miniPFRelIso_chg")
        df = df.Define("Muon_jetPtRatio", "getJetPtRatio(Muon_jetRelIso)")
        df = df.Define("Muon_jetBTagDeepFlavB", "ROOT::VecOps::Take(Jet_btagDeepFlavB,Muon_jetIdx,float(0.0))")
        df = df.Define("Muon_log_dxy", "ROOT::VecOps::log(abs(Muon_dxy))")
        df = df.Define("Muon_log_dz", "ROOT::VecOps::log(abs(Muon_dz))")
        
        df = df.Define("Electron_miniRelIsoNeutral", "Electron_miniPFRelIso_all - Electron_miniPFRelIso_chg")
        df = df.Define("Electron_jetPtRatio", "getJetPtRatio(Electron_jetRelIso)")
        df = df.Define("Electron_jetBTagDeepFlavB", "ROOT::VecOps::Take(Jet_btagDeepFlavB,Electron_jetIdx,float(0.0))")
        df = df.Define("Electron_log_dxy", "ROOT::VecOps::log(abs(Electron_dxy))")
        df = df.Define("Electron_log_dz", "ROOT::VecOps::log(abs(Electron_dz))")

        df = df.Define(
            "Lepton_MVAs",
            "evaluate_mva(Muon_pt, Muon_eta, Muon_pfRelIso03_all, Muon_miniPFRelIso_chg, Muon_miniRelIsoNeutral, Muon_jetNDauCharged, Muon_jetPtRelv2, Muon_jetPtRatio, Muon_jetBTagDeepFlavB, Muon_sip3d, Muon_log_dxy, Muon_log_dz, Muon_segmentComp, Muon_nStations, Muon_nTrackerLayers, Muon_highPurity, Muon_bsConstrainedChi2, Muon_tkRelIso, Electron_pt, Electron_eta, Electron_pfRelIso03_all, Electron_miniPFRelIso_chg, Electron_miniRelIsoNeutral, Electron_jetNDauCharged, Electron_jetPtRelv2, Electron_jetPtRatio, Electron_jetBTagDeepFlavB, Electron_sip3d, Electron_log_dxy, Electron_log_dz, Electron_mvaIso, Electron_lostHits, Electron_scEtOverPt, Electron_r9, Electron_sieie, Electron_hoe, Electron_eInvMinusPInv, Electron_dr03TkSumPt)"
        )
        
        df = df.Define("Muon_hwwMVA", "Lepton_MVAs[0]")
        df = df.Define("Electron_hwwMVA", "Lepton_MVAs[1]")
        
        df = df.DropColumns("Lepton_MVAs")

        return df
