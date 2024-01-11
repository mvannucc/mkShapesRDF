import ROOT
from mkShapesRDF.processor.framework.module import Module
from mkShapesRDF.processor.data.LeptonSel_cfg import *
import correctionlib
import os


class LeptonFakeWMaker(Module):
    def __init__(self, era):
        super().__init__("LeptonFakeWMaker")
        self.era = era

        self.mu_maxPt = 199.9
        self.mu_minPt = 15.001
        self.mu_maxEta = 2.3999
        self.mu_minEta = -2.3999

        self.el_maxPt = 499.99
        self.el_minPt = 10.001
        self.el_maxEta = 2.4999
        self.el_minEta = -2.4999

        self.LepFilter = LepFilter_dict
        self.ElectronWP = ElectronWP
        self.MuonWP = MuonWP

        self.cfg_path = os.path.dirname(os.path.dirname(__file__)).split("processor")[0]

        self.Fake_dict = {}

        # electron setup
        self.Fake_dict["electron"] = {}
        for wp in self.ElectronWP[self.era]["TightObjWP"]:
            self.Fake_dict["electron"][wp] = self.ElectronWP[self.era]["TightObjWP"][wp]["fakeW"]

        # muon setup
        self.Fake_dict["muon"] = {}
        for wp in self.MuonWP[self.era]["TightObjWP"]:
            self.Fake_dict["muon"][wp] = self.MuonWP[self.era]["TightObjWP"][wp]["fakeW"]

        print("LeptonFakeWMaker: Compute fake rates for  " + self.era)

    def runModule(self, df, values):

        #### DECLARE FORMULAS

        #### 
        #### Compute fake weight for 1 lepton   :   return 9-dim array with nominal + unc.
        ####

        ROOT.gInterpreter.Declare(
            """
            ROOT::RVecF getWeight_1l(float f, float f_up, float f_down, float fE, float p, int lep_id, int lep_pass){
                
                ROOT::RVecF fakeR_1l(9, 0.0);
             
                if ((p - f) == 0.0){
                    return fakeR_1l;
                }
   
                if (abs(lep_id)==13 && lep_pass==1){
                        
                    fakeR_1l[0] = (-1) * f * (1 - p) / (p - f); // Nom
                    fakeR_1l[1] = (-1) * f * (1 - p) / (p - f); // ElUp
                    fakeR_1l[2] = (-1) * f * (1 - p) / (p - f); // ElDown
                    fakeR_1l[3] = (-1) * f * (1 - p) / (p - f); // statElUp
                    fakeR_1l[4] = (-1) * f * (1 - p) / (p - f); // statElDown
                    fakeR_1l[5] = (-1) * f_up * (1 - p) / (p - f_up);         // MuUp
                    fakeR_1l[6] = (-1) * f_down * (1 - p) / (p - f_down);     // MuDown
                    fakeR_1l[7] = (-1) * (f + fE) * (1 - p) / (p - (f + fE)); // statMuUp
                    fakeR_1l[8] = (-1) * (f - fE) * (1 - p) / (p - (f - fE)); // statMuDown
                        
                }else if (abs(lep_id)==11 && lep_pass==1){
                    
                    fakeR_1l[0] = (-1) * f * (1 - p) / (p - f);
                    fakeR_1l[1] = (-1) * f_up * (1 - p) / (p - f_up);
                    fakeR_1l[2] = (-1) * f_down * (1 - p) / (p - f_down);
                    fakeR_1l[3] = (-1) * (f + fE) * (1 - p) / (p - (f + fE));
                    fakeR_1l[4] = (-1) * (f - fE) * (1 - p) / (p - (f - fE));
                    fakeR_1l[5] = (-1) * f * (1 - p) / (p - f);
                    fakeR_1l[6] = (-1) * f * (1 - p) / (p - f);
                    fakeR_1l[7] = (-1) * f * (1 - p) / (p - f);
                    fakeR_1l[8] = (-1) * f * (1 - p) / (p - f);
                    
                }else if (abs(lep_id)==13 && lep_pass!=1){
                    
                    fakeR_1l[0] = f * p / (p - f);
                    fakeR_1l[1] = f * p / (p - f);
                    fakeR_1l[2] = f * p / (p - f);
                    fakeR_1l[3] = f * p / (p - f);
                    fakeR_1l[4] = f * p / (p - f);
                    fakeR_1l[5] = f_up * p / (p - f_up);
                    fakeR_1l[6] = f_down * p / (p - f_down);
                    fakeR_1l[7] = (f + fE) * p / (p - (f + fE));
                    fakeR_1l[8] = (f - fE) * p / (p - (f - fE));
                    
                }else{
                    
                    fakeR_1l[0] = f * p / (p - f);
                    fakeR_1l[1] = f_up * p / (p - f_up);
                    fakeR_1l[2] = f_down * p / (p - f_down);
                    fakeR_1l[3] = (f + fE) * p / (p - (f + fE));
                    fakeR_1l[4] = (f - fE) * p / (p - (f - fE));
                    fakeR_1l[5] = f * p / (p - f);
                    fakeR_1l[6] = f * p / (p - f);
                    fakeR_1l[7] = f * p / (p - f);
                    fakeR_1l[8] = f * p / (p - f);
                    
                }
                return fakeR_1l;
            }
            """
        )
    


        ####
        #### Compute fake and prompt rates for 2 lepton   :   return [9-dim array, 9-dim array] with nominals and unc.
        ####

        ROOT.gInterpreter.Declare(
            """
            std::vector<ROOT::RVecF> getRate_2l(float f, float f_up, float f_down, float fE, float p, int lep_id, int lep_pass){
                
                std::vector<ROOT::RVecF> results;
                ROOT::RVecF fakeR_1l(9, 0.0);
                ROOT::RVecF promptR_1l(9, 0.0);
                
                if ((p - f) == 0.0){
                    results.push_back(fakeR_1l);
                    results.push_back(promptR_1l);
                    return results;
                }

                if (abs(lep_id)==13 && lep_pass==1){
                    
                    fakeR_1l[0] = f * (1 - p) / (p - f);
                    fakeR_1l[1] = f * (1 - p) / (p - f);
                    fakeR_1l[2] = f * (1 - p) / (p - f);
                    fakeR_1l[3] = f * (1 - p) / (p - f);
                    fakeR_1l[4] = f * (1 - p) / (p - f);
                    fakeR_1l[5] = f_up * (1 - p) / (p - f_up);
                    fakeR_1l[6] = f_down * (1 - p) / (p - f_down);
                    fakeR_1l[7] = (f + fE) * (1 - p) / (p - (f + fE));
                    fakeR_1l[8] = (f - fE) * (1 - p) / (p - (f - fE));
                    
                    promptR_1l[0] = p * (1 - f) / (p - f);
                    promptR_1l[1] = p * (1 - f) / (p - f);
                    promptR_1l[2] = p * (1 - f) / (p - f);
                    promptR_1l[3] = p * (1 - f) / (p - f);
                    promptR_1l[4] = p * (1 - f) / (p - f);
                    promptR_1l[5] = p * (1 - f_up) / (p - f_up);
                    promptR_1l[6] = p * (1 - f_down) / (p - f_down);
                    promptR_1l[7] = p * (1 - (f + fE)) / (p - (f + fE));
                    promptR_1l[8] = p * (1 - (f - fE)) / (p - (f - fE));
                    
                 }else if (abs(lep_id)==11 && lep_pass==1){

                     fakeR_1l[0] = f * (1 - p) / (p - f);
                     fakeR_1l[1] = f_up * (1 - p) / (p - f_up);
                     fakeR_1l[2] = f_down * (1 - p) / (p - f_down);
                     fakeR_1l[3] = (f + fE) * (1 - p) / (p - (f + fE));
                     fakeR_1l[4] = (f - fE) * (1 - p) / (p - (f - fE));
                     fakeR_1l[5] = f * (1 - p) / (p - f);
                     fakeR_1l[6] = f * (1 - p) / (p - f);
                     fakeR_1l[7] = f * (1 - p) / (p - f);
                     fakeR_1l[8] = f * (1 - p) / (p - f);
                     
                     promptR_1l[0] = p * (1 - f) / (p - f);
                     promptR_1l[1] = p * (1 - f_up) / (p - f_up);
                     promptR_1l[2] = p * (1 - f_down) / (p - f_down);
                     promptR_1l[3] = p * (1 - (f + fE)) / (p - (f + fE));
                     promptR_1l[4] = p * (1 - (f - fE)) / (p - (f - fE));
                     promptR_1l[5] = p * (1 - f) / (p - f);
                     promptR_1l[6] = p * (1 - f) / (p - f);
                     promptR_1l[7] = p * (1 - f) / (p - f);
                     promptR_1l[8] = p * (1 - f) / (p - f);
                     
                 }else if (abs(lep_id)==13 && lep_pass!=1){
                     
                     fakeR_1l[0] = f * p / (p - f);
                     fakeR_1l[1] = f * p / (p - f);
                     fakeR_1l[2] = f * p / (p - f);
                     fakeR_1l[3] = f * p / (p - f);
                     fakeR_1l[4] = f * p / (p - f);
                     fakeR_1l[5] = f_up * p / (p - f_up);
                     fakeR_1l[6] = f_down * p / (p - f_down);
                     fakeR_1l[7] = (f + fE) * p / (p - (f + fE));
                     fakeR_1l[8] = (f - fE) * p / (p - (f - fE));
                     
                     promptR_1l = fakeR_1l;
                     
                 }else{
                     
                     fakeR_1l[0] = f * p / (p - f);
                     fakeR_1l[1] = f_up * p / (p - f_up);
                     fakeR_1l[2] = f_down * p / (p - f_down);
                     fakeR_1l[3] = (f + fE) * p / (p - (f + fE));
                     fakeR_1l[4] = (f - fE) * p / (p - (f - fE));
                     fakeR_1l[5] = f * p / (p - f);
                     fakeR_1l[6] = f * p / (p - f);
                     fakeR_1l[7] = f * p / (p - f);
                     fakeR_1l[8] = f * p / (p - f);
                     
                     promptR_1l = fakeR_1l;
                 }
                results.push_back(fakeR_1l);
                results.push_back(promptR_1l);
                return results;
            }
            """
        )
                     
        
        ####
        #### Compute 2 lepton fake weight   :   return 9.dim array with nominal + unc.
        ####

        ROOT.gInterpreter.Declare(
            """
            ROOT::RVecF getWeight_2l(ROOT::RVecF f_mu, ROOT::RVecF f_mu_up, ROOT::RVecF f_mu_down, ROOT::RVecF fE_mu, ROOT::RVecF f_ele, ROOT::RVecF f_ele_up, ROOT::RVecF f_ele_down, ROOT::RVecF fE_ele, ROOT::RVecF p, ROOT::RVecI lep_id, ROOT::RVecI lep_Mupass, ROOT::RVecI lep_Elepass){
                
                ROOT::RVecF fakeR_2l(9, 0.0);
                ROOT::RVecF PF(9, 0.0);
                ROOT::RVecF FP(9, 0.0);
                ROOT::RVecF FF(9, 0.0);
                
                std::vector<ROOT::RVecF> fakeR_1;
                std::vector<ROOT::RVecF> fakeR_2;
                
                int nTight = 0;
                
                if (abs(lep_id[0])==13){
                    fakeR_1 = getRate_2l(f_mu[0], f_mu_up[0], f_mu_down[0], fE_mu[0], p[0], lep_id[0], lep_Mupass[0]);
                    if (lep_Mupass[0]==1) nTight += 1;
                }else{
                    fakeR_1 = getRate_2l(f_ele[0], f_ele_up[0], f_ele_down[0], fE_ele[0], p[0], lep_id[0], lep_Elepass[0]);
                    if (lep_Elepass[0]==1) nTight += 1;
                }
                
                if (abs(lep_id[1])==13){
                    fakeR_2 = getRate_2l(f_mu[1], f_mu_up[1], f_mu_down[1], fE_mu[1], p[1], lep_id[1], lep_Mupass[1]);
                    if (lep_Mupass[1]==1) nTight += 1;
                }else{
                    fakeR_2 = getRate_2l(f_ele[1], f_ele_up[1], f_ele_down[1], fE_ele[1], p[1], lep_id[1], lep_Elepass[1]);
                    if (lep_Elepass[1]==1) nTight += 1;
                }
                
                PF = fakeR_1[1] * fakeR_2[0];
                FP = fakeR_1[0] * fakeR_2[1];
                FF = fakeR_1[0] * fakeR_2[0];
                
                if (nTight==1){
                    FF *= -1;
                }else{
                    PF *= -1;
                    FP *= -1;
                }
                
                fakeR_2l = PF + FP + FF;
                return fakeR_2l;
            }
            """
        )


        #### 
        #### Compute 3 lepton fake weight   :   return 9.dim array with nominal + unc.
        ####
        
        ROOT.gInterpreter.Declare(
            """
            ROOT::RVecF getWeight_3l(ROOT::RVecF f_mu, ROOT::RVecF f_mu_up, ROOT::RVecF f_mu_down, ROOT::RVecF fE_mu, ROOT::RVecF f_ele, ROOT::RVecF f_ele_up, ROOT::RVecF f_ele_down, ROOT::RVecF fE_ele, ROOT::RVecF p, ROOT::RVecI lep_id, ROOT::RVecI lep_Mupass, ROOT::RVecI lep_Elepass){
                
                ROOT::RVecF fakeR_3l(9, 0.0);
                
                ROOT::RVecF PPF(9, 0.0);
                ROOT::RVecF PFP(9, 0.0);
                ROOT::RVecF FPP(9, 0.0);
                
                ROOT::RVecF PFF(9, 0.0);
                ROOT::RVecF FPF(9, 0.0);
                ROOT::RVecF FFP(9, 0.0);
                
                ROOT::RVecF FFF(9, 0.0);
                
                std::vector<ROOT::RVecF> fakeR_1;
                std::vector<ROOT::RVecF> fakeR_2;
                std::vector<ROOT::RVecF> fakeR_3;
                
                int nTight = 0;
                
                if (abs(lep_id[0])==13){
                    fakeR_1 = getRate_2l(f_mu[0], f_mu_up[0], f_mu_down[0], fE_mu[0], p[0], lep_id[0], lep_Mupass[0]);
                    if (lep_Mupass[0]==1) nTight += 1;
                }else{
                    fakeR_1 = getRate_2l(f_ele[0], f_ele_up[0], f_ele_down[0], fE_ele[0], p[0], lep_id[0], lep_Elepass[0]);
                    if (lep_Elepass[0]==1) nTight += 1;
                }
                
                if (abs(lep_id[1])==13){
                    fakeR_2 = getRate_2l(f_mu[1], f_mu_up[1], f_mu_down[1], fE_mu[1], p[1], lep_id[1], lep_Mupass[1]);
                    if (lep_Mupass[1]==1) nTight += 1;
                }else{
                    fakeR_2 = getRate_2l(f_ele[1], f_ele_up[1], f_ele_down[1], fE_ele[1], p[1], lep_id[1], lep_Elepass[1]);
                    if (lep_Elepass[1]==1) nTight += 1;
                }
                
                if (abs(lep_id[2])==13){
                    fakeR_3 = getRate_2l(f_mu[2], f_mu_up[2], f_mu_down[2], fE_mu[2], p[2], lep_id[2], lep_Mupass[2]);
                    if (lep_Mupass[2]==1) nTight += 1;
                }else{
                    fakeR_3 = getRate_2l(f_ele[2], f_ele_up[2], f_ele_down[2], fE_ele[2], p[2], lep_id[2], lep_Elepass[2]);
                    if (lep_Elepass[2]==1) nTight += 1;
                }
                
                PPF = fakeR_1[1] * fakeR_2[1] * fakeR_3[0];
                PFP = fakeR_1[1] * fakeR_2[0] * fakeR_3[1];
                FPP = fakeR_1[0] * fakeR_2[1] * fakeR_3[1];
                
                PFF = fakeR_1[1] * fakeR_2[0] * fakeR_3[0];
                FPF = fakeR_1[0] * fakeR_2[1] * fakeR_3[0];
                FFP = fakeR_1[0] * fakeR_2[0] * fakeR_3[1];
                
                FFF = fakeR_1[0] * fakeR_2[0] * fakeR_3[0];
                
                if (nTight==1 || nTight==3){
                    PPF *= -1.;
                    PFP *= -1.;
                    FPP *= -1.;
                    FFF *= -1.;
                }else{
                    PFF *= -1.;
                    FPF *= -1.;
                    FFP *= -1.;
                }
                
                fakeR_3l = PPF+PFP+FPP + PFF+FPF+FFP + FFF;
                
                return fakeR_3l;
            }
            """
        )

        
        #### 
        #### Compute 4 lepton fake weight   :   return 9.dim array with nominal + unc.
        ####

        ROOT.gInterpreter.Declare(
            """
            ROOT::RVecF getWeight_4l(ROOT::RVecF f_mu, ROOT::RVecF f_mu_up, ROOT::RVecF f_mu_down, ROOT::RVecF fE_mu, ROOT::RVecF f_ele, ROOT::RVecF f_ele_up, ROOT::RVecF f_ele_down, ROOT::RVecF fE_ele, ROOT::RVecF p, ROOT::RVecI lep_id, ROOT::RVecI lep_Mupass, ROOT::RVecI lep_Elepass){
                
                ROOT::RVecF fakeR_4l(9, 0.0);
                
                ROOT::RVecF PPPF(9, 0.0);
                ROOT::RVecF PPFP(9, 0.0);
                ROOT::RVecF PFPP(9, 0.0);
                ROOT::RVecF FPPP(9, 0.0);
                
                ROOT::RVecF FFPP(9, 0.0);
                ROOT::RVecF PPFF(9, 0.0);
                ROOT::RVecF PFPF(9, 0.0);
                ROOT::RVecF FPFP(9, 0.0);
                ROOT::RVecF FPPF(9, 0.0);
                ROOT::RVecF PFFP(9, 0.0);
                
                ROOT::RVecF FFFP(9, 0.0);
                ROOT::RVecF FFPF(9, 0.0);
                ROOT::RVecF FPFF(9, 0.0);
                ROOT::RVecF PFFF(9, 0.0);
                
                ROOT::RVecF FFFF(9, 0.0);
                
                std::vector<ROOT::RVecF> fakeR_1;
                std::vector<ROOT::RVecF> fakeR_2;
                std::vector<ROOT::RVecF> fakeR_3;
                std::vector<ROOT::RVecF> fakeR_4;
                
                int nTight = 0;
                
                if (abs(lep_id[0])==13){
                    fakeR_1 = getRate_2l(f_mu[0], f_mu_up[0], f_mu_down[0], fE_mu[0], p[0], lep_id[0], lep_Mupass[0]);
                    if (lep_Mupass[0]==1) nTight += 1;
                }else{
                    fakeR_1 = getRate_2l(f_ele[0], f_ele_up[0], f_ele_down[0], fE_ele[0], p[0], lep_id[0], lep_Elepass[0]);
                    if (lep_Elepass[0]==1) nTight += 1;
                }
                
                if (abs(lep_id[1])==13){
                    fakeR_2 = getRate_2l(f_mu[1], f_mu_up[1], f_mu_down[1], fE_mu[1], p[1], lep_id[1], lep_Mupass[1]);
                    if (lep_Mupass[1]==1) nTight += 1;
                }else{
                    fakeR_2 = getRate_2l(f_ele[1], f_ele_up[1], f_ele_down[1], fE_ele[1], p[1], lep_id[1], lep_Elepass[1]);
                    if (lep_Elepass[1]==1) nTight += 1;
                }
                
                if (abs(lep_id[2])==13){
                    fakeR_3 = getRate_2l(f_mu[2], f_mu_up[2], f_mu_down[2], fE_mu[2], p[2], lep_id[2], lep_Mupass[2]);
                    if (lep_Mupass[2]==1) nTight += 1;
                }else{
                    fakeR_3 = getRate_2l(f_ele[2], f_ele_up[2], f_ele_down[2], fE_ele[2], p[2], lep_id[2], lep_Elepass[2]);
                    if (lep_Elepass[2]==1) nTight += 1;
                }
                
                if (abs(lep_id[3])==13){
                    fakeR_4 = getRate_2l(f_mu[3], f_mu_up[3], f_mu_down[3], fE_mu[3], p[3], lep_id[3], lep_Mupass[3]);
                    if (lep_Mupass[3]==1) nTight += 1;
                }else{
                    fakeR_4 = getRate_2l(f_ele[3], f_ele_up[3], f_ele_down[3], fE_ele[3], p[3], lep_id[3], lep_Elepass[3]);
                    if (lep_Elepass[3]==1) nTight += 1;
                }
                
                PPPF = fakeR_1[1] * fakeR_2[1] * fakeR_3[1] + fakeR_4[0];
                PPFP = fakeR_1[1] * fakeR_2[1] * fakeR_3[0] + fakeR_4[1];
                PFPP = fakeR_1[1] * fakeR_2[0] * fakeR_3[1] + fakeR_4[1];
                FPPP = fakeR_1[0] * fakeR_2[1] * fakeR_3[1] + fakeR_4[1];
                
                FFPP = fakeR_1[0] * fakeR_2[0] * fakeR_3[1] + fakeR_4[1];
                PPFF = fakeR_1[1] * fakeR_2[1] * fakeR_3[0] + fakeR_4[0];
                PFPF = fakeR_1[1] * fakeR_2[0] * fakeR_3[1] + fakeR_4[0];
                FPFP = fakeR_1[0] * fakeR_2[1] * fakeR_3[0] + fakeR_4[1];
                FPPF = fakeR_1[0] * fakeR_2[1] * fakeR_3[1] + fakeR_4[0];
                PFFP = fakeR_1[1] * fakeR_2[0] * fakeR_3[0] + fakeR_4[1];
                
                FFFF = fakeR_1[0] * fakeR_2[0] * fakeR_3[0] + fakeR_4[0];
                
                if (nTight==1 || nTight==3){
                    FFPP *= -1.;
                    PPFF *= -1.;
                    PFPF *= -1.;
                    FPFP *= -1.;
                    FPPF *= -1.;
                    PFFP *= -1.;
                    FFFF *= -1.;
                }else{
                    PPPF *= -1.;
                    PPFP *= -1.;
                    PFPP *= -1.;
                    FPPP *= -1.;
                    FFFP *= -1.;
                    FFPF *= -1.;
                    FPFF *= -1.;
                    PFFF *= -1.;
                }
                
                fakeR_4l = PPPF+PPFP+PFPP+FPPP + FFPP+PPFF+PFPF+FPFP+FPPF+PFFP + FFFP+FFPF+FPFF+PFFF + FFFF;
                
                return fakeR_4l;
            }
            """
        )
    


        for ele_wp in self.Fake_dict["electron"]:
            for mu_wp in self.Fake_dict["muon"]:

                Tag = 'ele_'+ele_wp+'_mu_'+mu_wp

                eleDir = self.cfg_path + "/processor/" + self.Fake_dict["electron"][ele_wp]
                muDir = self.cfg_path + "/processor/" + self.Fake_dict["muon"][mu_wp]
                
                fileElPR = eleDir+'/ElePR.root'
                ElPR = 'h_Ele_signal_pt_eta_bin'
                
                fileElFR_jet25 = eleDir+'/EleFR_jet25.root'
                fileElFR_jet35 = eleDir+'/EleFR_jet35.root'
                fileElFR_jet45 = eleDir+'/EleFR_jet45.root'

                EleFR = 'FR_pT_eta_EWKcorr'
                MuFR = EleFR

                fileMuPR = muDir+'/MuonPR.root'
                MuPR = 'h_Muon_signal_pt_eta_bin'
                
                fileMuFR_jet10 = muDir+'/MuonFR_jet10.root'
                fileMuFR_jet15 = muDir+'/MuonFR_jet15.root'
                fileMuFR_jet20 = muDir+'/MuonFR_jet20.root'
                fileMuFR_jet25 = muDir+'/MuonFR_jet25.root'
                fileMuFR_jet30 = muDir+'/MuonFR_jet30.root'
                fileMuFR_jet35 = muDir+'/MuonFR_jet35.root'
                fileMuFR_jet45 = muDir+'/MuonFR_jet45.root'

                ####
                #### Open ROOT files and get fake rate TH1*
                ####

                ROOT.gInterpreter.Declare(
                    """
                    TFile* f_ele_PR_"""+Tag+f""" = TFile::Open("{fileElPR}");
                    TFile* f_mu_PR_"""+Tag+f"""  = TFile::Open("{fileMuPR}");
                    
                    TH2D* h_ele_PR_"""+Tag+""" = (TH2D*)f_ele_PR_"""+Tag+f"""->Get("{ElPR}");
                    TH2D* h_mu_PR_"""+Tag+"""  = (TH2D*)f_mu_PR_"""+Tag+f"""->Get("{MuPR}");
                    
                    TFile* f_ele_FR_jet25_"""+Tag+f""" = TFile::Open("{fileElFR_jet25}");
                    TFile* f_ele_FR_jet35_"""+Tag+f""" = TFile::Open("{fileElFR_jet35}");
                    TFile* f_ele_FR_jet45_"""+Tag+f""" = TFile::Open("{fileElFR_jet45}");
                    
                    TH2D* h_ele_FR_jet25_"""+Tag+""" = (TH2D*)f_ele_FR_jet25_"""+Tag+f"""->Get("{EleFR}");
                    TH2D* h_ele_FR_jet35_"""+Tag+""" = (TH2D*)f_ele_FR_jet35_"""+Tag+f"""->Get("{EleFR}");
                    TH2D* h_ele_FR_jet45_"""+Tag+""" = (TH2D*)f_ele_FR_jet45_"""+Tag+f"""->Get("{EleFR}");
                    
                    TFile* f_mu_FR_jet10_"""+Tag+f""" = TFile::Open("{fileMuFR_jet10}");
                    TFile* f_mu_FR_jet15_"""+Tag+f""" = TFile::Open("{fileMuFR_jet15}");
                    TFile* f_mu_FR_jet20_"""+Tag+f""" = TFile::Open("{fileMuFR_jet20}");
                    TFile* f_mu_FR_jet25_"""+Tag+f""" = TFile::Open("{fileMuFR_jet25}");
                    TFile* f_mu_FR_jet30_"""+Tag+f""" = TFile::Open("{fileMuFR_jet30}");
                    TFile* f_mu_FR_jet35_"""+Tag+f""" = TFile::Open("{fileMuFR_jet35}");
                    TFile* f_mu_FR_jet45_"""+Tag+f""" = TFile::Open("{fileMuFR_jet45}");
                    
                    TH2D* h_mu_FR_jet10_"""+Tag+""" = (TH2D*)f_mu_FR_jet10_"""+Tag+f"""->Get("{MuFR}");
                    TH2D* h_mu_FR_jet15_"""+Tag+""" = (TH2D*)f_mu_FR_jet15_"""+Tag+f"""->Get("{MuFR}");
                    TH2D* h_mu_FR_jet20_"""+Tag+""" = (TH2D*)f_mu_FR_jet20_"""+Tag+f"""->Get("{MuFR}");
                    TH2D* h_mu_FR_jet25_"""+Tag+""" = (TH2D*)f_mu_FR_jet25_"""+Tag+f"""->Get("{MuFR}");
                    TH2D* h_mu_FR_jet30_"""+Tag+""" = (TH2D*)f_mu_FR_jet30_"""+Tag+f"""->Get("{MuFR}");
                    TH2D* h_mu_FR_jet35_"""+Tag+""" = (TH2D*)f_mu_FR_jet35_"""+Tag+f"""->Get("{MuFR}");
                    TH2D* h_mu_FR_jet45_"""+Tag+""" = (TH2D*)f_mu_FR_jet45_"""+Tag+f"""->Get("{MuFR}");
                    """
                )

                ####
                #### Get fake rates for 1,2,3 or 4 leptons
                ####

                ROOT.gInterpreter.Declare(
                    """
                    std::vector<ROOT::RVecF> get_"""+Tag+"""_fake(ROOT::RVecF lep_pt, ROOT::RVecF lep_eta, ROOT::RVecI lep_id, ROOT::RVecI lep_MuTight, ROOT::RVecI lep_EleTight){

                        ROOT::RVecF p(lep_pt.size(), 1.0);
                        ROOT::RVecF f_10(lep_pt.size(), 0.0);
                        ROOT::RVecF f_15(lep_pt.size(), 0.0);
                        ROOT::RVecF f_20(lep_pt.size(), 0.0);
                        ROOT::RVecF f_25(lep_pt.size(), 0.0);
                        ROOT::RVecF f_30(lep_pt.size(), 0.0);
                        ROOT::RVecF f_35(lep_pt.size(), 0.0);
                        ROOT::RVecF f_45(lep_pt.size(), 0.0);

                        ROOT::RVecF pE(lep_pt.size(), 0.0);
                        ROOT::RVecF fE_10(lep_pt.size(), 0.0);
                        ROOT::RVecF fE_15(lep_pt.size(), 0.0);
                        ROOT::RVecF fE_20(lep_pt.size(), 0.0);
                        ROOT::RVecF fE_25(lep_pt.size(), 0.0);
                        ROOT::RVecF fE_30(lep_pt.size(), 0.0);
                        ROOT::RVecF fE_35(lep_pt.size(), 0.0);
                        ROOT::RVecF fE_45(lep_pt.size(), 0.0);

                        int nbins;
                        float ptmax;

                        std::vector<ROOT::RVecF> results;

                        ROOT::RVecF fakeR_1l_Mu20_Ele35(9, 0.0);
                        ROOT::RVecF fakeR_1l_Mu25_Ele35(9, 0.0);
                        ROOT::RVecF fakeR_1l_Mu35_Ele35(9, 0.0);

                        ROOT::RVecF fakeR_2l0j_Mu20_Ele35(9, 0.0);
                        ROOT::RVecF fakeR_2l1j_Mu25_Ele35(9, 0.0);
                        ROOT::RVecF fakeR_2l2j_Mu35_Ele35(9, 0.0);
                        ROOT::RVecF fakeR_3l_Mu35_Ele35(9, 0.0);
                        ROOT::RVecF fakeR_4l_Mu35_Ele35(9, 0.0);
                        
                        for (int i=0; i<lep_pt.size(); i++){

                            ptmax = 9999.9;
                            
                            if (abs(lep_id[i])==13){
                                
                                nbins = h_mu_PR_"""+Tag+"""->GetNbinsX();
                                ptmax = h_mu_PR_"""+Tag+"""->GetXaxis()->GetBinCenter(nbins);
                                
                                p[i] = h_mu_PR_"""+Tag+"""->GetBinContent(h_mu_PR_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], ptmax}), abs(lep_eta[i])));
                                pE[i] = h_mu_PR_"""+Tag+"""->GetBinError(h_mu_PR_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], ptmax}), abs(lep_eta[i])));
                                
                                f_10[i] = h_mu_FR_jet10_"""+Tag+"""->GetBinContent(h_mu_FR_jet10_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_10[i] = h_mu_FR_jet10_"""+Tag+"""->GetBinError(h_mu_FR_jet10_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                
                                f_15[i] = h_mu_FR_jet15_"""+Tag+"""->GetBinContent(h_mu_FR_jet15_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_15[i] = h_mu_FR_jet15_"""+Tag+"""->GetBinError(h_mu_FR_jet15_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                
                                f_20[i] = h_mu_FR_jet20_"""+Tag+"""->GetBinContent(h_mu_FR_jet20_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_20[i] = h_mu_FR_jet20_"""+Tag+"""->GetBinError(h_mu_FR_jet20_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                
                                f_25[i] = h_mu_FR_jet25_"""+Tag+"""->GetBinContent(h_mu_FR_jet25_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_25[i] = h_mu_FR_jet25_"""+Tag+"""->GetBinError(h_mu_FR_jet25_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                    
                                f_30[i] = h_mu_FR_jet30_"""+Tag+"""->GetBinContent(h_mu_FR_jet30_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_30[i] = h_mu_FR_jet30_"""+Tag+"""->GetBinError(h_mu_FR_jet30_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                    
                                f_35[i] = h_mu_FR_jet35_"""+Tag+"""->GetBinContent(h_mu_FR_jet35_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_35[i] = h_mu_FR_jet35_"""+Tag+"""->GetBinError(h_mu_FR_jet35_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                
                                f_45[i] = h_mu_FR_jet45_"""+Tag+"""->GetBinContent(h_mu_FR_jet45_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_45[i] = h_mu_FR_jet45_"""+Tag+"""->GetBinError(h_mu_FR_jet45_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                    
                            }else if(abs(lep_id[i])==11){

                                nbins = h_ele_PR_"""+Tag+"""->GetNbinsX();
                                ptmax = h_ele_PR_"""+Tag+"""->GetXaxis()->GetBinCenter(nbins);
                                
                                p[i] = h_ele_PR_"""+Tag+"""->GetBinContent(h_mu_PR_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], ptmax}), abs(lep_eta[i])));
                                pE[i] = h_ele_PR_"""+Tag+"""->GetBinError(h_mu_PR_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], ptmax}), abs(lep_eta[i])));
                                
                                f_25[i] = h_ele_FR_jet25_"""+Tag+"""->GetBinContent(h_ele_FR_jet25_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_25[i] = h_ele_FR_jet25_"""+Tag+"""->GetBinError(h_ele_FR_jet25_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                
                                f_35[i] = h_ele_FR_jet35_"""+Tag+"""->GetBinContent(h_ele_FR_jet35_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_35[i] = h_ele_FR_jet35_"""+Tag+"""->GetBinError(h_ele_FR_jet35_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                
                                f_45[i] = h_ele_FR_jet45_"""+Tag+"""->GetBinContent(h_ele_FR_jet45_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                fE_45[i] = h_ele_FR_jet45_"""+Tag+"""->GetBinError(h_ele_FR_jet45_"""+Tag+"""->FindBin(ROOT::VecOps::Min(ROOT::RVecF{lep_pt[i], 35.0}), abs(lep_eta[i])));
                                
                            }
                        }

                        if (lep_pt.size()==1){                        
                                if (abs(lep_id[0])==13){
                                fakeR_1l_Mu20_Ele35 = getWeight_1l(f_20[0], f_30[0], f_10[0], fE_20[0], p[0], lep_id[0], lep_MuTight[0]);
                                fakeR_1l_Mu25_Ele35 = getWeight_1l(f_25[0], f_35[0], f_15[0], fE_25[0], p[0], lep_id[0], lep_MuTight[0]);
                                fakeR_1l_Mu35_Ele35 = getWeight_1l(f_35[0], f_45[0], f_25[0], fE_35[0], p[0], lep_id[0], lep_MuTight[0]);
                            }else{
                                fakeR_1l_Mu20_Ele35 = getWeight_1l(f_35[0], f_45[0], f_25[0], fE_35[0], p[0], lep_id[0], lep_EleTight[0]);
                                fakeR_1l_Mu25_Ele35 = getWeight_1l(f_35[0], f_45[0], f_25[0], fE_35[0], p[0], lep_id[0], lep_EleTight[0]);
                                fakeR_1l_Mu35_Ele35 = getWeight_1l(f_35[0], f_45[0], f_25[0], fE_35[0], p[0], lep_id[0], lep_EleTight[0]);
                            }
                        }
                        if (lep_pt.size()>1){
                            fakeR_2l0j_Mu20_Ele35 = getWeight_2l(f_20, f_30, f_10, fE_20, f_35, f_45, f_25, fE_35, p, lep_id, lep_MuTight, lep_EleTight);
                            fakeR_2l1j_Mu25_Ele35 = getWeight_2l(f_25, f_35, f_15, fE_25, f_35, f_45, f_25, fE_35, p, lep_id, lep_MuTight, lep_EleTight);
                            fakeR_2l2j_Mu35_Ele35 = getWeight_2l(f_35, f_45, f_25, fE_35, f_35, f_45, f_25, fE_35, p, lep_id, lep_MuTight, lep_EleTight);  
                        }
                        if (lep_pt.size()>2){
                            fakeR_3l_Mu35_Ele35 = getWeight_3l(f_35, f_45, f_25, fE_35, f_35, f_45, f_25, fE_35, p, lep_id, lep_MuTight, lep_EleTight);
                        }
                        if (lep_pt.size()>3){
                            fakeR_4l_Mu35_Ele35 = getWeight_4l(f_35, f_45, f_25, fE_35, f_35, f_45, f_25, fE_35, p, lep_id, lep_MuTight, lep_EleTight);
                        }
                     
                        results.push_back(fakeR_1l_Mu20_Ele35);
                        results.push_back(fakeR_1l_Mu25_Ele35);
                        results.push_back(fakeR_1l_Mu35_Ele35);
                        results.push_back(fakeR_2l0j_Mu20_Ele35);
                        results.push_back(fakeR_2l1j_Mu25_Ele35);
                        results.push_back(fakeR_2l2j_Mu35_Ele35);
                        results.push_back(fakeR_3l_Mu35_Ele35);
                        results.push_back(fakeR_4l_Mu35_Ele35);
   
                        return results;
                    }
                    """
                )
                
                df = df.Define("fake_rates_"+Tag, "get_"+Tag+"_fake(Lepton_pt, Lepton_eta, Lepton_pdgId, Lepton_isTightMuon_"+mu_wp+", Lepton_isTightElectron_"+ele_wp+")")

                ##### 1 Lepton

                df = df.Define("fakeW_"+Tag+"1l_mu20_ele35", "fake_rates_"+Tag+"[0][0]")
                df = df.Define("fakeW_"+Tag+"1l_mu20_ele35_ElUp", "fake_rates_"+Tag+"[0][1]")
                df = df.Define("fakeW_"+Tag+"1l_mu20_ele35_ElDown", "fake_rates_"+Tag+"[0][2]")
                df = df.Define("fakeW_"+Tag+"1l_mu20_ele35_statElUp", "fake_rates_"+Tag+"[0][3]")
                df = df.Define("fakeW_"+Tag+"1l_mu20_ele35_statElDown", "fake_rates_"+Tag+"[0][4]")
                df = df.Define("fakeW_"+Tag+"1l_mu20_ele35_MuUp", "fake_rates_"+Tag+"[0][5]")
                df = df.Define("fakeW_"+Tag+"1l_mu20_ele35_MuDown", "fake_rates_"+Tag+"[0][6]")
                df = df.Define("fakeW_"+Tag+"1l_mu20_ele35_statMuUp", "fake_rates_"+Tag+"[0][7]")
                df = df.Define("fakeW_"+Tag+"1l_mu20_ele35_statMuDown", "fake_rates_"+Tag+"[0][8]")

                df = df.Define("fakeW_"+Tag+"1l_mu25_ele35", "fake_rates_"+Tag+"[1][0]")
                df = df.Define("fakeW_"+Tag+"1l_mu25_ele35_ElUp", "fake_rates_"+Tag+"[1][1]")
                df = df.Define("fakeW_"+Tag+"1l_mu25_ele35_ElDown", "fake_rates_"+Tag+"[1][2]")
                df = df.Define("fakeW_"+Tag+"1l_mu25_ele35_statElUp", "fake_rates_"+Tag+"[1][3]")
                df = df.Define("fakeW_"+Tag+"1l_mu25_ele35_statElDown", "fake_rates_"+Tag+"[1][4]")
                df = df.Define("fakeW_"+Tag+"1l_mu25_ele35_MuUp", "fake_rates_"+Tag+"[1][5]")
                df = df.Define("fakeW_"+Tag+"1l_mu25_ele35_MuDown", "fake_rates_"+Tag+"[1][6]")
                df = df.Define("fakeW_"+Tag+"1l_mu25_ele35_statMuUp", "fake_rates_"+Tag+"[1][7]")
                df = df.Define("fakeW_"+Tag+"1l_mu25_ele35_statMuDown", "fake_rates_"+Tag+"[1][8]")

                df = df.Define("fakeW_"+Tag+"1l_mu35_ele35", "fake_rates_"+Tag+"[2][0]")
                df = df.Define("fakeW_"+Tag+"1l_mu35_ele35_ElUp", "fake_rates_"+Tag+"[2][1]")
                df = df.Define("fakeW_"+Tag+"1l_mu35_ele35_ElDown", "fake_rates_"+Tag+"[2][2]")
                df = df.Define("fakeW_"+Tag+"1l_mu35_ele35_statElUp", "fake_rates_"+Tag+"[2][3]")
                df = df.Define("fakeW_"+Tag+"1l_mu35_ele35_statElDown", "fake_rates_"+Tag+"[2][4]")
                df = df.Define("fakeW_"+Tag+"1l_mu35_ele35_MuUp", "fake_rates_"+Tag+"[2][5]")
                df = df.Define("fakeW_"+Tag+"1l_mu35_ele35_MuDown", "fake_rates_"+Tag+"[2][6]")
                df = df.Define("fakeW_"+Tag+"1l_mu35_ele35_statMuUp", "fake_rates_"+Tag+"[2][7]")
                df = df.Define("fakeW_"+Tag+"1l_mu35_ele35_statMuDown", "fake_rates_"+Tag+"[2][8]")

                
                ##### 2 Lepton

                df = df.Define("fakeW_"+Tag+"_2l0j", "fake_rates_"+Tag+"[3][0]")
                df = df.Define("fakeW_"+Tag+"_2l0jElUp", "fake_rates_"+Tag+"[3][1]")
                df = df.Define("fakeW_"+Tag+"_2l0jElDown", "fake_rates_"+Tag+"[3][2]")
                df = df.Define("fakeW_"+Tag+"_2l0jstatElUp", "fake_rates_"+Tag+"[3][3]")
                df = df.Define("fakeW_"+Tag+"_2l0jstatElDown", "fake_rates_"+Tag+"[3][4]")
                df = df.Define("fakeW_"+Tag+"_2l0jMuUp", "fake_rates_"+Tag+"[3][5]")
                df = df.Define("fakeW_"+Tag+"_2l0jMuDown", "fake_rates_"+Tag+"[3][6]")
                df = df.Define("fakeW_"+Tag+"_2l0jstatMuUp", "fake_rates_"+Tag+"[3][7]")
                df = df.Define("fakeW_"+Tag+"_2l0jstatMuDown", "fake_rates_"+Tag+"[3][8]")

                df = df.Define("fakeW_"+Tag+"_2l1j", "fake_rates_"+Tag+"[4][0]")
                df = df.Define("fakeW_"+Tag+"_2l1jElUp", "fake_rates_"+Tag+"[4][1]")
                df = df.Define("fakeW_"+Tag+"_2l1jElDown", "fake_rates_"+Tag+"[4][2]")
                df = df.Define("fakeW_"+Tag+"_2l1jstatElUp", "fake_rates_"+Tag+"[4][3]")
                df = df.Define("fakeW_"+Tag+"_2l1jstatElDown", "fake_rates_"+Tag+"[4][4]")
                df = df.Define("fakeW_"+Tag+"_2l1jMuUp", "fake_rates_"+Tag+"[4][5]")
                df = df.Define("fakeW_"+Tag+"_2l1jMuDown", "fake_rates_"+Tag+"[4][6]")
                df = df.Define("fakeW_"+Tag+"_2l1jstatMuUp", "fake_rates_"+Tag+"[4][7]")
                df = df.Define("fakeW_"+Tag+"_2l1jstatMuDown", "fake_rates_"+Tag+"[4][8]")

                df = df.Define("fakeW_"+Tag+"_2l2j", "fake_rates_"+Tag+"[5][0]")
                df = df.Define("fakeW_"+Tag+"_2l2jElUp", "fake_rates_"+Tag+"[5][1]")
                df = df.Define("fakeW_"+Tag+"_2l2jElDown", "fake_rates_"+Tag+"[5][2]")
                df = df.Define("fakeW_"+Tag+"_2l2jstatElUp", "fake_rates_"+Tag+"[5][3]")
                df = df.Define("fakeW_"+Tag+"_2l2jstatElDown", "fake_rates_"+Tag+"[5][4]")
                df = df.Define("fakeW_"+Tag+"_2l2jMuUp", "fake_rates_"+Tag+"[5][5]")
                df = df.Define("fakeW_"+Tag+"_2l2jMuDown", "fake_rates_"+Tag+"[5][6]")
                df = df.Define("fakeW_"+Tag+"_2l2jstatMuUp", "fake_rates_"+Tag+"[5][7]")
                df = df.Define("fakeW_"+Tag+"_2l2jstatMuDown", "fake_rates_"+Tag+"[5][8]")

                ##### 3 Lepton

                df = df.Define("fakeW_"+Tag+"_3l", "fake_rates_"+Tag+"[6][0]")
                df = df.Define("fakeW_"+Tag+"_3lElUp", "fake_rates_"+Tag+"[6][1]")
                df = df.Define("fakeW_"+Tag+"_3lElDown", "fake_rates_"+Tag+"[6][2]")
                df = df.Define("fakeW_"+Tag+"_3lstatElUp", "fake_rates_"+Tag+"[6][3]")
                df = df.Define("fakeW_"+Tag+"_3lstatElDown", "fake_rates_"+Tag+"[6][4]")
                df = df.Define("fakeW_"+Tag+"_3lMuUp", "fake_rates_"+Tag+"[6][5]")
                df = df.Define("fakeW_"+Tag+"_3lMuDown", "fake_rates_"+Tag+"[6][6]")
                df = df.Define("fakeW_"+Tag+"_3lstatMuUp", "fake_rates_"+Tag+"[6][7]")
                df = df.Define("fakeW_"+Tag+"_3lstatMuDown", "fake_rates_"+Tag+"[6][8]")

                ##### 4 Lepton

                df = df.Define("fakeW_"+Tag+"_4l", "fake_rates_"+Tag+"[7][0]")
                df = df.Define("fakeW_"+Tag+"_4lElUp", "fake_rates_"+Tag+"[7][1]")
                df = df.Define("fakeW_"+Tag+"_4lElDown", "fake_rates_"+Tag+"[7][2]")
                df = df.Define("fakeW_"+Tag+"_4lstatElUp", "fake_rates_"+Tag+"[7][3]")
                df = df.Define("fakeW_"+Tag+"_4lstatElDown", "fake_rates_"+Tag+"[7][4]")
                df = df.Define("fakeW_"+Tag+"_4lMuUp", "fake_rates_"+Tag+"[7][5]")
                df = df.Define("fakeW_"+Tag+"_4lMuDown", "fake_rates_"+Tag+"[7][6]")
                df = df.Define("fakeW_"+Tag+"_4lstatMuUp", "fake_rates_"+Tag+"[7][7]")
                df = df.Define("fakeW_"+Tag+"_4lstatMuDown", "fake_rates_"+Tag+"[7][8]")
                
                df = df.DropColumns("fake_rates_"+Tag)
                
        

        return df
