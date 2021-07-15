#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import scipy
import check_array_element

# [AF,GE,GREF,DELTAX,DELTAY] = ARRAYGAIN (PHI,TH,PHI0,TH0,AD,ED)
#
#   Power gain of a phased array in direction PHI, TH (radians)
#   when the array is phase-steered to PHI0, TH0 (radians).
#   The structure AD describes the array and ED its element.
#
#   The angle TH can be a vector.
#
#   The structure AD describes the array geometry:
#
#     .Mx is number of elements in X-direction.
#     .My is number of elements in Y-direction
#     .Dx is element spacing in X-direction, in units of wavelenght.
#     .Dy is element spacing in Y-direction, in units of wavelenght.
#
#   AD can be [], then only the element gain GE is computed.
#       
#   The structure ED describes the element:
#     
#     .phi    is the azimuth angle (counterclockwise from positive x) 
#             of element beam direction.
#     .th is  the polar angle of the elements beam direction.
#     .width  is the element's half power beam width (radians).
#     .gain   is the element's gain.
#             (only either .width or .gain should to be given, 
#             the other quantity is computed.)
#
#   ED can be [], then only the array factor is computed.
#
#   Return values:
#
#   AF is the array factor, normalized to unity in broadside
#   direction.
#   GE is the element gain factor, normalized  to max value unity
#   in the element optical axis direction ED.phi,ED.th. 
#   GREF is the power gain of the antenna in the vertical direction
#        when all the elements are also in vertical direction.
#   DELTAX and DELTAY are the "unwrapped" phasing angles required
#   to achieve the required beam direction. Values outside [-pi,pi]
#   mean that the beam [PHI0,TH0] is some of the "grating" beams 
#   (but who cares).
#
#   From AF, GE and GREF, the antenna power gain can then 
#   be computed as
#
#       G = GREF * GE .* AF .^ 2
#
#   The functions DIRIC from the signal processing toolbox and
#   CHECK_ARRAY_ELEMENT from the e3dant package are needed.
#
#   The function PLAINARRAY can be used for plotting the array gain.

def arraygain(PHI,TH,PHI0,TH0,AD,ED):

    if not (ED.size == 0):
        ED = check_array_element(ED)
        nE   = ED.n
        Ephi = ED.phi
        Eth  = ED.th
        Ebw  = ED.width
        Ge0  = ED.gain

        # Rotate the element's pattern to the array coordinate system.

        # (1) The Element's direction vector coordinates in the array
        #     system are

        Ue = np.array([np.sin(Eth) * np.cos(Ephi), np.sin(Eth) * np.sin(Ephi), np.cos(Eth)])

        # (2) Matrix rr, where a column gives the direction vector
        #     r for a single th.

        rr = np.array([np.sin(th) * np.cos(phi), np.sin(th) * np.sin(phi), np.cos(th)])

        # (3) An element's normalized gain as function of theta, 
        #     as a row vector

        Ge = (0.5 * (1 + Ue * rr)) ** (nE/2)

    else:
        Ge = 1
        Ge0 = 1

    if not (AD.size == 0):
        Mx = AD.Mx
        My = AD.My
        Dx = AD.Dx
        Dy = AD.Dy

        # (4) Get the unwrapped phase steering angles deltaX and deltaY
        #  that give (some) array beam into the direction phi0, th0:
        #
        #   deltaX = 2pi u0_x Dx
        #   deltaY = 2pi u0_y Dy
        #
        # where
        #
        #   u0_x = sin(th0) cos(phi0)
        #   u0_y = sin(th0) sin(phi0) 

        deltaX = 2 * np.pi * np.sin(th0) * np.cos(phi0) * Dx
        deltaY = 2 * np.pi * np.sin(th0) * np.sin(phi0) * Dy

        # (5) Array factor, normalized to unity in the array broadside
        #     direction.

        PsiX = 2 * pi * Dx * np.cos(phi) * np.sin(th) - deltaX
        PsiY = 2*pi*Dy*sin(th)*sin(phi) - deltaY
        AFx = abs(scipy.special.diric(PsiX,Mx))
        AFy = abs(scipy.special.diric(PsiY,My))
        AF = AFx * AFy;
    else:
        Mx = 1
        My = 1
        delta_X = 0
        delta_Y = 0
        AF = 1

    # (6) Use as a reference gain the broadside gain with the elements
    #     vertical.

    Gref = Ge0 * Mx * My

    return AF,GE,GREF,DELTAX,DELTAY


# In[ ]:




