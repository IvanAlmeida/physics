# -*- coding: utf-8 -*-
"""
This is an auxiliary script with handful constants.
Everything is on cgs (Astronomers...)
"""
import math as mt

#-------------------- Natural constants --------------------
#light speed
c = 3*pow(10,10)

#Planck constant
hp = 6.626*pow(10,-27)

#Barred Planck constant
hbar = hp/(2*mt.pi) 

#Gravitational constant
gn = 6.67*pow(10,-8)

#Electron charge
ec = 4.80*pow(10,-10)

#electron mass
me = 9.1093897*pow(10,-28)

#proton mass
mp = 1.672623*pow(10,24)

#neutron mass
mn = 1.6749*pow(10,-24)

#hydrogen mass
mh = 1.6733*pow(10,-24)

#Radiation density constant
rdc = 7.56*pow(10,-15)

#Steffan-Boltzmann constant
sb = 5.67*pow(10,-5)

#Fine structure constant
alpha_fs = 7.30*pow(10,-3)

#Rydberg constant
ryd = 2.18*pow(10,-11)

#Thomson cross section
sig_th = 6.65*pow(10,-25)

#-----------------------------------------------------------

#-----------------Scaling Values----------------------------

#Atomic mass unit
amu = 1.66*pow(10,-24)

#Avogrado Number
an = 6.022*pow(10,23)

#Boltzmann constant
kb = 1.38*pow(10,-16)

#1eV in cgs
ev = 1.602*pow(10,-12)

#Bohr radius
a0 = hbar**2/(me*ec**2)

#-----------------------------------------------------------

#-----------------------Astronomy---------------------------
#Astronomical unit
au = 1.496*pow(10,13)

#Parsec
pc = 3.086*pow(10,18)

#Light year
ly = 9.463*pow(10,17)

#Solar mass
msun = 1.99*pow(10,33)

#Solar radius
rsun = 6.96*pow(10,10)

#Solar Luminosity
lsun = 3.9*pow(10,33)

#-----------------------------------------------------------
