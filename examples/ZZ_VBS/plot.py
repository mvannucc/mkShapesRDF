

groupPlot = {}


#groupPlot['DY']  = {  
#    'nameHR' : "DY",
#    'isSignal' : 0,
#    'color'    : 418,    # kGreen+2
#    'samples'  : ['dyll']
#}

plot = {}
# keys here must match keys in samples.py    
                    
plot['dyll']  = {  
    'nameHR'   : 'DY',
    'color'    : 418,    # kGreen+2
    'isSignal' : 0,
    'isData'   : 0, 
    'scale'    : 1.0,
}

plot['ZZZ']  = {
    'nameHR'   : 'ZZZ',
    'color'    : 218,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['WZZ']  = {
    'nameHR'   : 'WZZ',
    'color'    : 218,  
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['WWZ']  = {
    'nameHR'   : 'WWZ',
    'color'    : 218,  
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['TTZToLLNuNu_M-10']  = {
    'nameHR'   : 'ttZ',
    'color'    : 118,   
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ggZZ4e']  = {
    'nameHR'   : 'ggZZ4e',
    'color'    : 518,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ggZZ4mu']  = {
    'nameHR'   : 'ggZZ4mu',
    'color'    : 518,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ggZZ2e2mu']  = {
    'nameHR'   : 'ggZZ2e2mu',
    'color'    : 518,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ZZjj4l']  = {
    'nameHR'   : 'ZZjj4l',
    'color'    : 318,    # kGreen+2
    'isSignal' : 1,
    'isData'   : 0,
    'scale'    : 1.0,
}

# data

plot['DATA']  = { 
    'nameHR'   : 'Data',
    'color'    : 1 ,  
    'isSignal' : 0,
    'isData'   : 1 ,
    'isBlind'  : 0
}




# additional options
legend = {}

legend['lumi'] = 'L =  59.8 fb^{-1}'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
