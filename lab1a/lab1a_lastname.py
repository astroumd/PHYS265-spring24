#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:26:27 2022
Modified on Fri Mar 11 15:26:27 2022
@author: Your name

Description
------------
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from lab1a_utilities import calculate_force
from lab1a_utilities import calculate_potential

# Create the source charges


# Set the default initial conditions for v0, angle, and y0
v0, angle, y0 = 50.0, 30.0, 30.0    
# Keep x0 fixed at -100
x0 = -100.

def clear():
    
    # NO NEED TO EDIT THIS FUNCTION

    fig = plt.figure('Game Window')
    ax = fig.axes[0]
    ax.cla()
    ax.axis('square')
    ax.set_xlim(-200,200)
    ax.set_ylim(-200,200)
    ax.set_title('Electrostatic Projectile Game',fontsize=16)
    ax.set_xlabel('x position (meters)',fontsize=16)
    ax.set_ylabel('y position (meters)',fontsize=16)
    ax.grid(visible=True)
    fig.tight_layout()    
    fig.show()
    return
fig = plt.figure('Game Window')
ax = fig.add_subplot()
clear()


############################################################

def play():

    # NO NEED TO EDIT THIS FUNCTION

    global v0, angle, y0
    
    print("Starting x location is -100")
    v0 = float(input("Enter the initial speed between zero and 100.\n"))
    assert(v0 >= 0 and v0 <= 100), "Initial velocity should > 0 and < 100"
    angle = float(input("Enter the initial angle in degrees.\n"))
    assert(angle >= -180.00 and angle <= 180.00), \
        "Angle should be between -180 and +180"
    y0 = float(input("Enter the initial y position.\n"))
    assert(y0 >= -200 and y0 <= 200), "y0 should be between -200 and +200"
    
    plot_trajectory()
    
    return
 


############################################################

def reveal_potential():

    fig = plt.figure('Game Window')
    # for a 3D wireframe or surface plot, comment out this line:
    ax = fig.axes[0]
# Uncomment these lines to create a 3D wireframe or surface plot
#    fig.clf()
#    ax = fig.add_subplot(projection='3d')

    # your code goes here


    return

############################################################

def reveal_forcefield():
    fig = plt.figure('Game Window')
    ax = fig.axes[0]
    
    # your code goes here


    return

############################################################


############################################################

def plot_trajectory():

    fig = plt.figure('Game Window')
    ax = fig.axes[0]
    
    # Your code goes here


    return

############################################################

def solve_it():

        
    return









