#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Author:   Peter Teuben
Created:  Tue Mar 12 20:11:06 2024
Modified: Tue Mar 12 20:11:06 2024

Description:
------------
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import quad
from scipy.integrate import solve_ivp

#%% some constants

try:
    
    import no_astropy.units as u
    from astropy.constants import G, M_earth, R_earth
    
    print("astropy variables defined")

    R = R_earth
    M = M_earth
    print(G, M, R)

    g = G * M_earth / R_earth**2
    print('g =',g)

    Torbit = 2*np.pi*np.sqrt(R**3/(G*M))
    print('torbit =',Torbit)
    print('       =',Torbit.to(u.min))

    rho0 = M_earth / (4*np.pi*R_earth**3/3)
    print("rho0 =",rho0)
    vorbit = np.sqrt(G*M_earth/R_earth)
    print('vorbit =',vorbit)

    vrotate = 2*np.pi*R_earth/(24*3600*u.s)
    print('vrotate =',vrotate.to('km/s'))
    
    #  in the code we actually can't always use astropy units
    #  so  we convert back to just the values in SI units
    g = g.value
    M_earth = M_earth.value
    R_earth = R_earth.value
    M_moon  = 7.35e+22        # kg
    R_moon  = 1738.1 * 1000   # m
except:
    print("sorry, no astropy here, using values in SI units")
    M_earth = 5.972e+24       # kg
    R_earth = 6378.1 * 1000   # m
    M_moon  = 7.35e+22        # kg
    R_moon  = 1738.1 * 1000   # m
    G = 6.6743e-11            # m3 / (kg s2)
    g = G * M_earth / R_earth**2
    
    print("g =", g)
    
#%% Useful Functions for this lab

def zero(x, y, level=0, debug=False):
    """ simple level finder using manual looping and linear interpolation
    
        x:       input X array
        y:       input Y array
        level:   value in the Y array to find
        zero:    the interpolated X coordinate where level was found
        
        Note that 0.0 is returned when the Y array didn't seem to cross level
    """
    z = y - level          # thus find the 0 crossing in xz
    n = len(t)             # t and x should have the same length
    s0 = np.sign(z[0])
    for i in range(1,n):
        if np.sign(z[i]) != s0:
            if debug: print(f"Changed sign at {i}/{n}")
            s0 = 0
            break
    if s0 == 0:
        if debug: print(x[i-1],x[i],z[i-1],z[i])
        # linear interpolation
        return x[i-1] - z[i-1]*(x[i]-x[i-1])/(z[i]-z[i-1])
    # if it failed to find a change of sign, return 0
    return 0.0

def density(r, n=0):
    """ return density of the earth in normalized units.
    
    Function should be vectorizable, as it needs to be used by quad()
    
    r:         input radius, must be in [0,1]
    density:   output density, will be [0,1]
    """
    return (1-r**2)**n

#%%  First constant gravity drop, theoretical and by integration
#    This creates Figure 1. No drag.

def freefall_time(height):
    """
    return the time in seconds for an object to drop a given height
    in meters, given constant gravity (g)
    """
    # return
    
def derivatives_gravc(t, s, drag=0):
    """ Derivatives D[2] for moving in a constant gravity field
    """
    # return D
    
 
# print("Expected free fall time, no drag",freefall_time(r0))

sol1 = solve_ivp()  # fill in the rest

    
plt.figure(1)
plt.clf()
plt.title(f"constant gravity, depth={r0} drag={drag}")

print("Final pos/vel:", sol1.y[0][-1],sol1.y[1][-1])
print("zero level at t=",zero(t,sol1.y[0]))

#%% Next falling into a weaker gravitation field of the homogeneous earth
#   This creates Figure 2.

def derivatives_homogeneous(t, s, drag=0):
    """ solve_ivp() derivatives for a homogeneous density earth with optional drag
    """
    # return D
    

sol2 = solve_ivp(derivatives_homogeneous)   # fill in the rest

plt.figure(2)
plt.clf()
plt.legend()  
plt.title(f"homogeneous earth")

print("Final pos/vel:", sol2.y[0][-1],sol2.y[1][-1])
print("zero level at t=",zero(t,sol2.y[0]))

#%% Now add a coriolis force, for a hole dug along the equator
#   This creates Figure 3.

# this will be a 2D problem, make a plot showing the ball in X-Y space,
# where X will be the depth into the earth, and Y along the width of the hole
# Presumably your plot will cover 4000m in X, and 5m in Y, with auto-scaling
# to clearly show the effect of the coriolis force 

def derivatives_coriolis(t, s):
    """ solve_ivp() derivatives for a homogeneous density earth with coriolis forces
    """    
    # return D

x0,y0,vx0,vy0 = r0,0,0,0

#%% Now we dig the hole through the earth, from North pole to South pole
#   This creates Figure 4.

#%% We will now change the density profile of the earth (1-r^2)^n
#   This creates Figure 5, 6, 7

def derivatives_earth(t, s, n=0):
    """ solve_ivp() derivatives for a non-homogeneous density earth
    """    
    # return D

    
#  Try these figures for a few values of n (0,1,2, but also 10, and maybe 100?)
#  Is the integration accurate enough for higher values of n ?
#  What is the meaning of a higher value of n?

#  Figure 5:  plot density as function of radius

#  Figure 6:  plot force as function of radius

#  Figure 7:  plot radius and velocity along the hole as function of time

#%% Consider the moon, but just a constant density moon. 
#   No figure needed, just the time difference between earth and moon 
#   travel time to the center. Maybe write a function for this

def travel_to_center(mass, radius):
    # return
