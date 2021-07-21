#!/usr/bin/env python
# coding: utf-8

# In[14]:


def simplegain( phi, th, ED):

    # G = SIMPLEGAIN (PHI, TH, ED)
    #
    # Normalized gain in direction PHI (azimuth, radians) and TH (polar angle)
    # of an antenna element described by the element descriptor ED.
    #
    # This implementation requires the following fields in ED.
    #
    #   .phi        # element azimuth
    #   .th         # element polar angle
    #   .gain       # element power gain, as multiplicative factor
    #   .width      # element halfpower beamwidth
    #
    # TH can be a row vector, PHI must be scalar.
    #
    # 23-Oct-2005 Jm
    #######################################################################

    nargin = (len(args) + len(kwargs))

    if nargin != 3:
        print('Bad number of parameters')

    G0    = ED.gain
    nE    = 2 * G0 - 2
    Ephi  = ED.phi
    Eth   = ED.th
    
    n = len(th)
    m = len(th[0])
    
    if n > 1:
        print('TH must be a row vector')

    # Rotate the element's pattern to the array coordinate system.

    # The Element's direction vector coordinates in the array system are

    Ue = np.array([np.sin(Eth) * np.cos(Ephi), np.sin(Eth) * np.sin(Ephi), np.cos(Eth)],ndmin=2)

    #  Matrix rr, where a column gives the direction vector r for a single th.

    rr = np.array([np.sin(th) * np.cos(phi), np.sin(th) * np.sin(phi), np.cos(th)],ndmin=2).transpose()

    # An element's normalized gain as function of theta, as a row vector

    G = (0.5 * (1 + Ue*rr)) ** (nE/2)

    return G, G0




# In[12]:


import numpy as np
a = np.array([1, 2, 3],ndmin=2).transpose()


# In[13]:


a


# In[ ]:




