#!/usr/bin/env python
# coding: utf-8

# In[10]:


#W = BEAMWIDTH (DX,DY,MX,MY,PHI0,TH0,LEVEL)
#
# Find the (up-down) beamwidth, in the vertical phi=PHI0 plane, 
# of a 2D-phased array with element spacing DX and DY (in units of
# wavelength) and MX and MY element in the X- and Y-directions,
# phase steered to direction PHI0 and TH0 (radians).
# TH0 can be a vector.
# 
# The returned beamwidth W corresponds to the width of
# the beam at the LEVEL, which must be  0 < LEVEL < 1.
# If LEVEL is not given, 0.5 is used.
#
# We solve for th+, th- the beamshape equation 
#
#   diric(psiX,Mx) * diric(psiY,My) = +- sqrt(level)  
# 
# with
#
#   psiX = 2*pi*Dx*cos(psi0) * (u-u0)
#   psiY = 2*pi*Dy*sin(psi0) * (u-u0)
#
# where u = sin(th), u0 = sin(th0).
#
# Values of TH0 that are too near to +-pi/2 return W=NaN.

import numpy as np
import scipy
from scipy.optimize import fsolve

def fun(x,A,B,Mx,My,level):
    
    return abs (scipy.special.diric(A*x,Mx) * scipy.special.diric(B*x,My)) - level
        
def beamwidth(Dx,Dy,Mx,My,phi0,th0,level):
    nargin = (len(args) + len(kwargs))

    if nargin < 6 or nargin > 8:
        print(error ('Bad number of arguments'))
    elif nargin == 6:
        level = 0.5

    # First find the value X (= u - u0) where
    #
    #   diric(A*X,Mx)*diric(B*X,My) = sqrt(level)

    A = abs(2*np.pi*np.cos(phi0) * Dx)
    B = abs(2*np.pi*np.sin(phi0) * Dy)

    if A != 0:
        a = 1/(Mx*A)
    else:
        a = np.inf
    
    if B != 0:
        b = 1/(My*B)
    else:
        b = np.inf

    
    X0 = np.array([0, 2 * np.pi * np.min([a,b])])

    X = fsolve(fun(x),X0)

    # Then find the points u1 and u2 where
    #
    # {+/-}X = u{2/1} - u0 

    u0 = np.sin(th0)
    u1 = u0 - X
    u2 = u0 + X

    # Then convert from u to theta.

    th2 = np.arcsin(u2)
    th1 = np.arcsin(u1)

    w = th2 - th1

    # Flag the illegal points as NaNs.

    w[(abs(u1) > 1) or (abs(u2) > 1)] = np.nan
    
    return w


# In[ ]:




