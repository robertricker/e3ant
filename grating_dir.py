#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np

def grating_dir(Dx, Dy, deltaX, deltaY):
    
    # Find all grating lobe directions with kz >= 0. We return the
    # unit vectors giving the lobe directions.
    #
    # The first element [X(1),Y(1),Z(1)] gives the main beam direction.
    #
    # We solve the direction of the unit vector
    #
    #    u = [x, y, z]  = (kx,ky,kz)/||k||
    #
    # from
    #
    #   x = kx/k = nx/Dx + deltaX/(2pi Dx)
    #   y = ky/k = ny/Dy + deltaY/(2pi Dy)
    #
    # where n1 and n2 must be such that
    #
    #   x^2 + y^2 <= 1
    #
    # so that we get z from  
    #
    #   z = +sqrt( 1 - x^2 + y^2);
    #


    #
    # 14-Oct-2005 Jm
    ####################################################################


    # Find the "bounding box" for (nx, ny) by requiring that
    # 
    #   -1 <= x <= 1 and   -1 <= y <= 1

    Nx = np.arange(np.ceil(-deltaX/(2*np.pi) - Dx), np.floor(-deltaX/(2*np.pi) + Dx), 1)
    Ny = np.arange(np.ceil(-deltaY/(2*np.pi) - Dy), np.floor (-deltaY/(2*np.pi) + Dy),1)

    # Then go trough all (nx,ny) in the box

    m = 0
    X = []
    Y = []
    Z = []
    x0 = np.nan
    
    for ny in Ny[np.arange(-1,0,-1)]:
        for nx in Nx:
            x = (nx*2*np.pi + deltaX)/(2*np.pi*Dx)
            y = (ny*2*np.pi + deltaY)/(2*np.pi*Dy)
            z2 = 1 - x**2 - y**2
            if z2 >= 0:
                z = sqrt (z2)
                if nx == 0 and ny == 0:
                    x0 = x
                    y0 = y
                    z0 = z
                else:
                    X[m] = x
                    Y[m] = y
                    Z[m] = z
                    m = m+1
                    
    if ~np.isnan(x0):
        X = np.append(x0,X)
        Y = np.append(y0,Y)
        Z = np.append(z0,Z)
    
    return X,Y,Z

