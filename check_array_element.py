#!/usr/bin/env python
# coding: utf-8

import numpy as np

# Compute missing fields of array element descriptor.
#
# Array element's gain pattern parameters G0 and n for the 
# generic approximative pattern, in the elements principal axis system
#
#   G = G0*[cos(th/2)]^n
#
# At input, ED must have fields
#
#   .phi            azimuth angle (radians), measured c-clockw from x-ax.
#   .th             polar angle (radians)
#   .gain           (multiplicative power gain)
#   .width          (half power beam width, radians)
#
# One or the other, but not both, of the last two fields must be empty.  

def check_array_element(ED):
    
    n = []

    if (not "width" in ED) or (ED.width.size == 0):
        if (not "gain" in ED) or (ED.gain.size == 0):
            print('arraygain: Either element gain or beamwidth must be specified')
        else:
            n = 2*ED.gain - 2;
            ED.width = 4 * np.arccos( (0.5)**(1/n) )

    if (not "gain" in ED) or (ED.gain.size == 0):
        if (not "width" in ED) or (ED.width.size == 0):
            print('arraygain: Either element gain or beamwidth must be specified')
        else:
            n = np.log10(0.5) / np.log10 (np.cos((ED.width/2)/2));
            ED.gain = (n+2)/2

    if n.size == 0:
        ED.n = np.log10(0.5) / np.log10(np.cos((ED.width/2)/2))
    else:
        ED.n = n
        
    return ED

