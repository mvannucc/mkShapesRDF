Red=625; Cyan=422; Violet=880; Green=418; Orange=800; Yellow=391; Azure=860

groupPlot = {}

plot = {}

# keys here must match keys in samples.py                        

plot['SM'] = {
    'nameHR'   : 'SM',
    'color'    : Orange,  # Example: Use different colors for linear and quadratic
    'isSignal' : 0,  # Change to 1 if it's a signal process
    'isData'   : 0,  # Change to 1 if it's data
    'scale'    : 1.0,  # Adjust the scaling if needed
}

plot['lin_cHWB'] = {
    'nameHR'   : 'lin cHWB', 
    'color'    : Green,  # Example: Use different colors for linear and quadratic
    'isSignal' : 1,  # Change to 1 if it's a signal process 
    'isData'   : 0,  # Change to 1 if it's data
    'scale'    : 1.0,  # Adjust the scaling if needed
}

plot['quad_cHWB'] = {
    'nameHR'   : 'quad cHWB',
    'color'    : Violet,  
    'isSignal' : 1,  # Change to 1 if it's a signal process
    'isData'   : 0,  # Change to 1 if it's data
    'scale'    : 1.0,  # Adjust the scaling if needed
}

# Iterate over operators and weights to populate the plot dictionary
#for operator in operators.keys():
#    for weight in weights:
#        sample_name = f'{weight}_{operator}'
#        plot[sample_name] = {
#            'nameHR'   : f'ZZ VBS EFT ({weight}, {operator})',
#            'color'    : 'Red' if weight == 'lin' else 'Blue',  # Example: Use different colors for linear and quadratic
 #           'isSignal' : 1,  # Change to 1 if it's a signal process
 #           'isData'   : 0,  # Change to 1 if it's data
 #           'scale'    : 1.0,  # Adjust the scaling if needed
 #       }

# additional options
legend = {}

legend['lumi'] = 'L =  59.8 fb^{-1}'

legend['sqrt'] = '#sqrt{s} = 13 TeV'

legend['extra'] = {
    'text': 'Your extra legend text here',
    'position': [0.7, 0.85, 0.9, 0.9],  # [x1, y1, x2, y2] in NDC coordinates
    'textSize': 0.03,                   # Optional: text size
    'font': 42,                         # Optional: font type (e.g., 42 for Helvetica)
    'color': 1                          # Optional: text color (ROOT color index)
}
