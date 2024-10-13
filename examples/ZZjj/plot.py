Cyan=432; Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860

groupPlot = {}

plot = {}

# keys here must match keys in samples.py                        

plot['Fake_lep']  = {
    'color'    : Red,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['VVZ']  = {
    'nameHR'   : 'VVZ',
    'color'    : Azure,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ttZ']  = {
    'nameHR'   : 't#bar{t}Z',
    'color'    : Yellow,   
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ggZZ']  = {
    'nameHR'   : 'gg #rightarrow ZZ',
    'color'    : Green,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ZZTo2Q2L']  = {
    'nameHR'   : 'ZZ #rightarrow 2l2q',
    'color'    : Cyan,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ZZ4L']  = {
    'nameHR'   : 'q#bar{q} #rightarrow ZZ',
    'color'    : Violet,    
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ZZjj4l']  = {
    'nameHR'   : 'ZZjj4l',
    'color'    : Orange,
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
