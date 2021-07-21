#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

def simplebeam():

    d2r = np.pi/180
    r2d = 180/np.pi

    W=np.empty(2)
    n=np.empty(2)
    G0=np.empty(2)

    W[0] = 40 * d2r
    n[0] = np.log10(0.5) / np.log10(np.cos((W[0]/2)/2))
    G0[0] = (n[0]+2)/2

    G0[1]= 10
    n[1] = 2 * G0[1] - 2
    W[1] = 4 * np.arccos( (0.5)**(1/n[1] ))

    G0_dB = 10*np.log10(G0)
    Wdeg = W*r2d

        # Polar-angle grid

    th1 = -90 * d2r
    th2 = 90 * d2r
    th_step = 0.001 * d2r 
    th = np.arange(th1,th2,th_step)

    # Compute the element's directivity (=max power gain) G0, assuming 
    # insignificant side-lobes in the cos^ny (theta/2) beam power gain pattern.
    # (This is found by requiring that the pattern integrates to 4pi.)
    
    G = []
    G_dB = []

    for k in np.arange(2):
        G.append(G0[k] * np.cos(th/2) ** n[k])
        G_dB.append(10 * np.log10 (G[k]))

    plt.subplot(211)
    plt.plot(th*r2d, G[0]/G0[0],'r--')
    plt.plot(th*r2d, th*r2d, G[1]/G0[1],'b-')
    plt.ylim(-30,20)
    plt.xlim(th1*r2d,th2*r2d)
    plt.xlabel('$\theta (\circ)$')
    plt.ylabel('G/Ge')
    plt.show()

simplebeam()

