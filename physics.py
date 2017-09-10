# -*- coding: utf-8 -*-
"""
This is an auxiliary script with handful constants and useful functions.
Everything is on cgs (Astronomers...)
"""

import math as mt
import numpy as np



c = 3*pow(10,10)

hp = 6.626*pow(10,-27)

hbar = hp/(2*mt.pi) 

Gn = 6.67*pow(10,-8)

ec = 4.80*pow(10,-10)

me = 9.11*pow(10,-28)

mn = 1.6749*pow(10,-24)

mh = 1.6733*pow(10,-24)

amu = 1.66*pow(10,-24)

Na = 6.022*pow(10,23)

kb = 1.38*pow(10,-16)

ev = 1.602*pow(10,-12)

rdc = 7.56*pow(10,-15)

sb = 5.67*pow(10,-5)

alpha_fs = 7.30*pow(10,-3)

ryd = 2.18*pow(10,-11)

au = 1.496*pow(10,13)

pc = 3.086*pow(10,18)

ly = 9.463*pow(10,17)

msun = 1.99*pow(10,33)

rsun = 6.96*pow(10,10)

lsun = 3.9*pow(10,33)

a0 = hbar**2/(me*ec**2)

sig_th = 6.65*pow(10,-25)

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

  ni0 = c/(lambd*pow(10,-8))

  sigma0 = (1-mt.exp((hp*ni0)/(kb*T)))*f

  return(sigma0)


def saha(logpe, logb1, logb2, Te, i1):

  lognn = -logpe -0.48 + mt.log10(2*logb2/logb1) +2.5*mt.log10(Te) - 5040*i1/Te
  return(lognn)

def energies_bohr(ni, nf,Z):

  delta_E = -Z**2*13.6*(1/nf**2 - 1/ni**2)

  return(delta_E)
  

def freq_bohr(ni1,nf1,Z_atom1):

  #freq em GHz

  freq = (energies_bohr(ni1,nf1,Z_atom1)*ev/hp)/10**9

  return(freq)
  

def v_term(Temperature,mass):

  v_th = mt.sqrt(2*kb*Temperature/mass)

  return(v_th)


def rad_to_deg(rad):

  deg = 180*rad/mt.pi

  return(deg)



def deg_to_rad(degree):

  radi = mt.pi*degree/180

  return(radi)
