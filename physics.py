# -*- coding: utf-8 -*-
"""
This is an auxiliary script with useful functions.
Everything is on cgs (Astronomers...)
"""

import math as mt
import numpy as np
from constants import *

# ====================================================================

def blackbody(ni,Tb):
    '''
Planck Law, the blackbody function.
Enter frequency in Hz and Temperature in K
Returns radiance
    '''
    Ebb =hp*ni/(kb*Tb)
    BB  =(2*hp*ni**3/c**2)/(mt.exp(Ebb)-1)
    return(BB)

def RayleighJeans(nu, T):
    '''
Rayleigh-Jeans law
Enter frequency in Hz and Temperature in K
Returns Radiance
    '''
    rj = (2*kb*T/c**2)*nu**2
    return (rj)


def sigma(lambd,f,T):
  '''
I don't remember what is this...
  '''
  ni0 = c/(lambd*pow(10,-8))

  sigma0 = (1-mt.exp((hp*ni0)/(kb*T)))*f

  return(sigma0)


def saha(logpe, b1, b2, Te, i1):
  '''
Saha equation
Enter logpe = log10[Pressure = N_e KT], b1 and b2 are the degenerescencies, Te temperature in Kelvin an i1 is the ionization energy from ith state.
Returns log[N2/N1], N2 is the number of ions in i+1 state, and N1 the number of ions in i state.
  '''
  lognn = -logpe -0.48 + mt.log10(2*b2/b1) +2.5*mt.log10(Te) - 5040*i1/Te
  return(lognn)

def energies_bohr(ni, nf,Z_atom=1):
  '''
Calculates the Bohr energy transitions for given states.
Enter ni = initial stage, nf = final stage and Z_atom = atomic number. Hydrogen is the default.
Return energy transition in eV. Negative value is absorption, positive value is emission.
  '''
  delta_E = -Z_atom**2*13.6*(1/nf**2 - 1/ni**2)

  return(delta_E)
  

def freq_bohr(ni1,nf1,Z_atom1):
  '''
Calculates photon's frequency of an atomic transition for given states.
Enter ni1 = initial stage, nf1 = final stage and Z_atom1 = atomic number. Hydrogen is the default.
Return frequency em GHz. Negative value is absorption, positive value is emission.
  '''
  freq = (energies_bohr(ni1,nf1,Z_atom1)*ev/hp)/10**9

  return(freq)
  

def v_term(Temperature,mass):
  '''
Calculate thermal velocity of a thermal system.
Enter Temperature in K and mass i g
Returns v_thermal im cm/s
  '''
  v_th = mt.sqrt(2*kb*Temperature/mass)

  return(v_th)

def schwarzschild_radius(mass):
  '''
Calculates the Schwarzchild radius from given mass
Return is Solar Radius
  '''
  r_s0 = 2*Gn*mass/c**2
  #Solar mass Schwarszchild radius
  r_s_sun = 2*Gn*msun/c**2
  r_s = r_s0/r_s_sun
  return (r_s)
  
def mass_sw_bh(radius):
  '''
Calculates the BH's mass from Schwarzchild radius in cm
Return is Solar masses
  '''
  mass = (radius*c**2/(Gn*2))/msun
  return(mass)
  
def eddington_lum(mass):
  '''
Calculates Eddington luminosity of determined BH mass
Returns in Solar luminosities
  '''
  l_e = 1.3e38*(mass/msun)/lsun
  return l_e

def accretion_rate(luminosity, eta = 0.1):
  '''
Calculating accretion rate of a BH, using efficiency eta and measured luminosity.
Output im msun/year.
  '''
  mdot = luminosity/(eta*c**2)
  #passando para msun/ano
  m_dot = (mdot/msun)*3.154e7
  return m_dot

# =========== Astronomical Unit Conversions =============

def rad_to_deg(rad):
  '''
Converts radians to degrees
  '''
  deg = 180*rad/mt.pi

  return(deg)

def deg_to_rad(degree):
  '''
Converts degrees to radians
  '''
  radi = mt.pi*degree/180

  return(radi)

def rad_to_as(rad):
  '''
Converts radians to arcsecs
  '''
  arcsec = rad_to_deg(rad)*3600
  return(arcsec)
  
def as_to_rad(arcsec):
  '''
Converts arcsecs to radians
  '''
  rad = deg_to_rad(arcsec/3600)
  return(rad)

def cm_to_pc(cm):
  '''
Converts cm to pc
  '''
  parsec = pc*cm
  return(parsec)
  
def pc_to_cm(psc):
  '''
Converts pc to cm
  '''
  centimeter = psc/pc
  return(centimeter)
