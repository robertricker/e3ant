#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import math 
#import check_array_element
#import simplegain

def cart2sph(x,y,z):
    XsqPlusYsq = x**2 + y**2
    r = math.sqrt(XsqPlusYsq + z**2)               # r
    elev = math.atan2(z,math.sqrt(XsqPlusYsq))     # theta
    az = math.atan2(y,x)                           # phi
    
    return az, elev

def powerint( AD, ED, phi0, theta0):

    # [P,D] = POWERINT ( AD, ED, PHI0, THETA0)
    #
    # Evaluate the power integral and directivity of a phased array.
    #
    # This version assumes unit excitation amplitudes.
    #
    #   Structure AD is the array descriptor, which must contain
    #   at least the fields
    #       .Dx , the element spacing in x-direction in units of wavelength
    #       .Dy , the element spacing in y-direction
    #       .Mx , number of elements in x-direction
    #       .My , number of elemetns in y-direction
    #       
    #   Structure ED is the antenna element descriptor, as specified in
    #   check_array_element.m.
    #
    #   (PHI0, THETA0) is the azimuth and polar angle of (some) phase-steered
    #   beam in radians.

    #
    # 3-Nov-2005 Jm
    #######################################################################

    nargin = (len(args) + len(kwargs))
    if nargin != 4:
        print('bad number of input arguments')

    # Pick the needed fields from the descriptors.

    ED = check_array_element(ED)
    nE   = ED.n
    Ephi = ED.phi
    Eth  = ED.th
    Ebw  = ED.width
    Ge0  = ED.gain

    Dx = AD.Dx
    Dy = AD.Dy
    Mx = AD.Mx
    My = AD.My  

    # Find the grating directions. Note that the first element
    # of the return vector refers to the grating beam in direction Phi0, Theta0.

    deltaX = 2 * np.pi * np.sin(theta0) * np.cos(phi0) * Dx
    deltaY = 2 * np.pi * np.sin(theta0) * np.sin(phi0) * Dy
    Ux,Uy,Uz = grating_dir(Dx,Dy, deltaX, deltaY)
    Ph, El = cart2sph(Ux,Uy,Uz)
    Th = pi/2 - El

    # Evaluate the element gain in the grating directions.
    
    GE=np.empty(len(Ph))
    for g in np.arange(0,len(Ph)):
        GE[g] = simplegain( Ph[g], Th[g], ED)

    # Evaluate the grating sum. 

    Grsum = sum( GE / np.cos(Th) )

    # Compute the powerintegral (assuming all a_m = 1).

    P = Grsum * Mx * My / ( 4 * np.pi * Dx * Dy )

    # Compute the array directivity.

    D = 4 * np.pi * Mx * My * Dx * Dy * GE[0] / Grsum

    return P, D








# In[ ]:




