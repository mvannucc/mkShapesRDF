# structure configuration for datacard

structure = {}

# keys here must match keys in samples.py    
#                   

structure['ZZJJTo4L_EFT']  = {
                  'isSignal' : 1,
                  'isData'   : 0
              }

structure['ZZJJTo4L_EWK']  = {
                  'isSignal' : 1,
                  'isData'   : 0
              }

structure['ZZJJTo4L_QCD']  = {
                  'isSignal' : 1,
                  'isData'   : 0
              }

structure['ZZ4L']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['ggZZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['ttZ4']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['VVZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

#structure['Fake_e']  = {  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'removeFromCuts' : [ k for k in cuts if 'me' in k],
#              }

#structure['Fake_m']  = {  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'removeFromCuts' : [ k for k in cuts if 'em' in k],
#              }

# data

structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }
