# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:47:30 2024

@author: gcart
"""
import  numpy as np
import matplotlib.pyplot as plt

# IT SHOULD NOT BE NECESSARY TO MODIFY THESE FUNCTIONS.
# IT SHOULD NOT BE NECESSARY TO COPY AND PASTE THESE FUNCTIONS
# INTO ANOTHER FILE.

# TO USE THESE FUNCTIONS DO
# import lab1GameUtilities as l1
# l1.calculate_potential(x,y,mycharges)
# l1.calculate_force(x,y,mycharges)

############################################################

def calculate_potential(x, y, hidden_charges):
    """
    calculate_potential() returns the total electrostatic potential
    due to the charges hidden in the xy plane.

    Input Parameters
    ----------
    x : 
        TYPE: a single floating point number.
        DESCRIPTION: this is the x coordinate where the force
        will be computed.
    y : 
        TYPE: a single floating point number.
        DESCRIPTION: this is the y coordinate where the force
        will be computed.
    hidden_charges : 
        TYPE: a 2D numpy array having three columns.The number
        of rows is the number of hidden charges in the xy plane.
        Ex: if there are five charges hidden in the plane, 
        then there will be five rows.
        DESCRIPTION. Each row describes one hidden charge. 
            The first column in the magnitude of the hidden charge.
            The second column is the x coordinate of the hidden charge.
            The third colunmn is the y coordinate of the hidden charge.
    Returns
    -------
    Vee :
        TYPE: a single floating point number
        DESCRIPTION: the total scalar potential at location x, y. 

    """

    k = 1000.0
    Vee = 0.0

    Q = hidden_charges[:,0] # magnitudes of the hidden charges.
    Qx = hidden_charges[:,1] # x coordinates of the hidden charges.
    Qy = hidden_charges[:,2] # y coordinates of the hidden charges.

    for i in range(len(Q)):
        distance = np.sqrt((x-Qx[i])**2 + (y-Qy[i])**2)
        if not np.isclose(distance,0.0):
            Vee = Vee + k*Q[i]*np.log(1.0/distance)

    return Vee

############################################################

def calculate_force(x,y,hidden_charges):
    """
    calculate_force() returns Fx and Fy, the x and y components
    of the electrostatic force caused by the hidden charges on a
    projectile.The projectile is assumed to have charge = +1.

    See the docstring for calculate_force() for a description of the 
    input parameters.

    Returns
    -------
    Fx, Fx are the x and y components of the force experienced by
    the projectile.
    """

    k = 1000.0
    Fx = 0.0
    Fy = 0.0

    Q = hidden_charges[:,0]
    Qx = hidden_charges[:,1]
    Qy = hidden_charges[:,2]

    for i in range(len(Q)):
        distance_sqrd = (x-Qx[i])**2 + (y-Qy[i])**2
        if not np.isclose(distance_sqrd,0.0):
            Fx = Fx + k*Q[i]*(x-Qx[i])/distance_sqrd
            Fy = Fy + k*Q[i]*(y-Qy[i])/distance_sqrd

    return Fx, Fy




