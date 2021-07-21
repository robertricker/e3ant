#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

def simple_vhfbeam(Eoffs, Noffs):

    # G = SIMPLE_VHFBEAM (Eoffs, Noffs)
    #
    # Gain pattern of vertical EISCAT VHF beam.
    # EOFFS is the offset along the short intersection (E-W for vertical beam).
    # NOFFS is the offset along long intersection (N-W for vertical beam).
    # Return the relative power gain (relative to beam center) G, using
    # Gaussian approximation with the 3dB points as hardcoded here.

    # 6-Sep-2006 Jm
    ###############################################################

    #N-S angular size 1.7 degr
    #E-W angular size 0.6 degr 

    aNS = (1.7/2) * np.pi/180
    aEW = (0.6/2) * np.pi/180


    b2EW = (10/3) * np.log10(np.exp(1)) * aEW**2
    b2NS = (10/3) * np.log10(np.exp(1)) * aNS**2

    g = exp ( -Eoffs**2 / b2EW  - Noffs**2 / b2NS )
    
    return g

