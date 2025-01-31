from math import sin, sqrt
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from animation import animateFunction

def simulation(f_start, omega_start):
    """
        Variables
    """
    f = f_start
    omega = omega_start
    y = 0
    t = 0
    yDot = 0 # assumtion

    k = 40*1e3
    m = 100
    c = 500
    g = 9.81
    t_delta = 1e-4

    # range
    func_start = 0
    func_stop = 2

    y_values = []
    yDot_values = []
    yDotDot_values = []
    t_values = []

    while t < func_stop:
        """
            Calculate new values
        """
        # Forces
        F = f*sin(omega * t) # external force
        G = m*g
        y_delta = (y) 
        S = k * (y_delta)
        yDot_delta = yDot
        D = c * yDot_delta

        # Integrals
        yDotDot = (1/m)*(F-G-D-S)
        yDot = yDot + t_delta * yDotDot
        y = y + t_delta * yDot
        
        """
            Record values
        """
        yDotDot_values.append(yDotDot)
        yDot_values.append(yDot)
        y_values.append(y)
        t_values.append(t)

        """
            Update values
        """
        t += t_delta # next t

    return t_values, y_values, yDot_values, yDotDot_values
    
"""
    Plots
"""
fig, axs = plt.subplots(2, 2)
fig.suptitle("Max y, Max yDot, RMS y, RMS yDot")

# a)
t_values, y_values, yDot_values, yDotDot_values = simulation(0, 0)
axs[0, 0].plot(t_values, y_values)
axs[0, 0].set_title(f'a) {max(y_values):.2f}, {max(yDot_values):.2f}, {sqrt((1/len(y_values)) * sum([x**2 for x in y_values])):.2f}, {sqrt((1/len(yDot_values)) * sum([x**2 for x in yDot_values])):.2f}')
xy_points = [(0.0, y) for y in y_values]
animateFunction(xy_points, 2, "./lecture_1_2/opp4/", "a")

# b)
t_values, y_values, yDot_values, yDotDot_values = simulation(500, 10)
axs[0, 1].plot(t_values, y_values)
axs[0, 1].set_title(f'b) {max(y_values):.2f}, {max(yDot_values):.2f}, {sqrt((1/len(y_values)) * sum([x**2 for x in y_values])):.2f}, {sqrt((1/len(yDot_values)) * sum([x**2 for x in yDot_values])):.2f}')
xy_points = [(0.0, y) for y in y_values]
animateFunction(xy_points, 2, "./lecture_1_2/opp4/", "b")

# c)
t_values, y_values, yDot_values, yDotDot_values = simulation(500, 20)
axs[1, 0].plot(t_values, y_values)
axs[1, 0].set_title(f'c) {max(y_values):.2f}, {max(yDot_values):.2f}, {sqrt((1/len(y_values)) * sum([x**2 for x in y_values])):.2f}, {sqrt((1/len(yDot_values)) * sum([x**2 for x in yDot_values])):.2f}')
xy_points = [(0.0, y) for y in y_values]
animateFunction(xy_points, 2, "./lecture_1_2/opp4/", "c")

# d)
t_values, y_values, yDot_values, yDotDot_values = simulation(500, 30)
axs[1, 1].plot(t_values, y_values)
axs[1, 1].set_title(f'd) {max(y_values):.2f}, {max(yDot_values):.2f}, {sqrt((1/len(y_values)) * sum([x**2 for x in y_values])):.2f}, {sqrt((1/len(yDot_values)) * sum([x**2 for x in yDot_values])):.2f}')
xy_points = [(0.0, y) for y in y_values]
animateFunction(xy_points, 2, "./lecture_1_2/opp4/", "d")

plt.show()