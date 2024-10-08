# structure configuration for datacard

structure = {}

# keys here must match keys in samples.py    
#                   

structure['ZZjj_4l']  = {
                  'isSignal' : 1,
                  'isData'   : 0
              }

structure['dyll']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['ggZZ4e']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['ggZZ4mu']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['ggZZ2e2mu']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['Fake_e']  = {  
                  'isSignal' : 0,
                  'isData'   : 0,
#                  'removeFromCuts' : [ k for k in cuts if 'me' in k],
              }

structure['Fake_m']  = {  
                  'isSignal' : 0,
                  'isData'   : 0,
#                  'removeFromCuts' : [ k for k in cuts if 'em' in k],
              }

structure['top'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['WWjj_QCD']  = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  }

structure['WWewk_CMWW_LL']  = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['WWewk_CMWW_LT']  = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['WWewk_CMWW_TL']  = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['WWewk_CMWW_TT']  = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['ggWW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['Wg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['Vg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VgS'] = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VgS_L'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['VgS_H'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['Zg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['WZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['VVV']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['ZZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['qqH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }
