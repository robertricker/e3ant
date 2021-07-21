#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

def testarray_snr():

# TESTARRAY_SNR
#   Compute SNR for the Kiruna test array
#
#   
#

# 22-Sep-2006 Jm
#################################################################### 

    H = 120

    if H == 120:

        Elev = 29.9            # Elevation (not used here, for documentation only)

        Vol_km3 = 155          # Effective volume, km^3            
        Vol70_km3 = 67         # max Effective volume for 70 usec pulse
        Vol30_km3 = 30         # max Effective volume for 30 usec pulse

        G0_array_dB = 25.4     # Test array directivity in dB
        TX = 1e6               # VHF peak power
        Rt = 120e3             # VHF range to common volume
        Rr = 233e3             # Test array range to common volume (from geom prog)
        Ne = 1e11              # Electron density
        lam = 3e8/224e6     # Radar wavelength
        Tsys = 150             # Receiver noise temp
        Brec = 20e3            # Receiver bandwidth

        chi = 31.7*np.pi/180      # Angle between E-field and scattering direction (rad) 
                                # (Taken from EISCAT geom program)
    elif H == 300:

        Elev = 55.0            # Elevation (not used here, for documentation only)

        Vol_km3 = 1340          # Effective volume, km^3            
        Vol70_km3 = 342         # max Effective volume for 70 usec pulse

        G0_array_dB = 28       # Test array directivity in dB
        TX = 1e6               # VHF peak power
        Rt = 300e3             # VHF range to common volume
        Rr = 364e3             # Test array range to common volume (from geom prog)
        Ne = 1e11              # Electron density
        lam = 3e8/224e6     # Radar wavelength
        Tsys = 150             # Receiver noise temp
        Brec = 20e3            # Receiver bandwidth ???

        chi = 56.8*pi/180      # Angle between E-field and scattering direction (rad) 
                                # (Taken from EISCAT geom program)
    elif H == 600:

        Elev = 70.0            # Elevation (not used here, for documentation only)

        Vol_km3 = 13600         # Effective volume, km^3            
        Vol70_km3 = 1250        # max Effective volume for 70 usec pulse

        G0_array_dB = 28.5     # Test array directivity in dB
        TX = 1e6               # VHF peak power
        Rt = 600e3             # VHF range to common volume
        Rr = 634e3             # Test array range to common volume (from geom prog)
        Ne = 1e11              # Electron density
        lam = 3e8/224e6     # Radar wavelength
        Tsys = 150             # Receiver noise temp
        Brec = 20e3            # Receiver bandwidth

        chi = 71.8*np.pi/180      # Angle between E-field and scattering direction (rad) 
                                # (Taken from EISCAT geom program)

    elif H == 1000:

        Elev = 77.0            # Elevation (not used here, for documentation only)

        Vol_km3 = 13600         # Effective volume, km^3            
        Vol70_km3 = 1250        # max Effective volume for 70 usec pulse

        G0_array_dB = 26.1     # Test array directivity in dB
        TX = 1e6               # VHF peak power
        Rt = 1000e3            # VHF range to common volume
        Rr = 1022e3            # Test array range to common volume (from geom prog)
        Ne = 1e11              # Electron density
        lam = 3e8/224e6     # Radar wavelength
        Tsys = 150             # Receiver noise temp
        Brec = 20e3            # Receiver bandwidth

        chi = 78.8*np.pi/180      # Angle between E-field and scattering direction (rad) 
                                # (Taken from EISCAT geom program)

    else:
        print('Unsupported altitude value')

    # --------------------------------------------------------

    Vol = Vol_km3 * 1e9      # effective volume m^3

    polfactor = np.sin(chi)**2

    A_VHF = 3000;                       # VHF eff area
    G0_VHF = 4*np.pi*A_VHF/lam**2       # VHF antenna gain
    G0_KIR = 10**(G0_array_dB/10)       # Test array directivity

    G0_VHF_db = 10*np.log10(G0_VHF)


    # Bistatic radar equation for received signal power

    sigma0 = 1e-28 * polfactor
    A = TX * lam**2 * G0_VHF * G0_KIR / ( Rt**2 * Rr**2 * (4*np.pi)**3 ) 
    B = Vol * Ne * sigma0  # total backscatter cross section
    Psig = A * B

    # Noise power

    kB = 1.38e-23

    Pnoise = kB * Tsys * Brec

    # Signal-to-noise ration

    SNR = Psig/Pnoise

    SNR_70 = SNR * Vol70_km3/Vol_km3
    
    return SNR, SNR_70, Pnoise, G0_VHF_db, Vol

