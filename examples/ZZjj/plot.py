groupPlot = {}

plot = {}

# keys here must match keys in samples.py                        

plot['VVZ']  = {
    'nameHR'   : 'VVZ',
    'color'    : 416,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ttZ']  = {
    'nameHR'   : 't#bar{t}Z',
    'color'    : 400,   
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ggZZ']  = {
    'nameHR'   : 'gg #rightarrow ZZ',
    'color'    : 600,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ZZ4L']  = {
    'nameHR'   : 'q#bar{q} #rightarrow ZZ',
    'color'    : 880,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ZZjj4l']  = {
    'nameHR'   : 'ZZjj4l',
    'color'    : 800,
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
