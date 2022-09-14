from math import pi, sin, cos, tanh
import matplotlib.pyplot as plt
from animation import animateFunction
import numpy as np

"""
    Constants
"""
m_1 = 2000 # kg
m_2 = 400 # kg
L_0 = 500/1000 # 500mm / 1000 = 0.5 m
k = 100*1000 # 100kN/m * 1000 = 100000 N/m
b = 1500 # N*s/m
h = 800/1000 # 800mm = 0.8m
h_0 = 3100/1000 # 3100mm = 3.1m
g = 9.81 # m/s^2

"""
    Variables
"""
t_delta = 0.001
t = 0 # s
t_end = 5
x_1 = 500/1000 # 500mm 0.5m
x_2 = 1800/1000 # 1800mm 1.8m
xDot_1 = 0 # m/s
xDot_2 = 0 # m/s
xDotDot_1 = 0 # m/s
xDotDot_2 = 0 # m/s

t_values = []
x_1_values = []
xDot_1_values = []
xDotDot_1_values = []

x_2_values = []
xDot_2_values = []
xDotDot_2_values = []

# using levels 0-2 to count the springs and dempers
while t < t_end:
    """
        x_1
    """
    # level 1 deltas
    level_1_k_delta = x_2 - (x_1+h)
    level_1_b_delta = xDot_2 - xDot_1

    F_mg_m1 = -g*m_1 # force of gravity
    # level 0
    F_k0_m1 = x_1 * k # lowest spring
    F_b0_m1 = xDot_1 * b # lowest demper
    # level 1
    F_k1_m1 = level_1_k_delta * k # lowest spring
    F_b1_m1 = level_1_b_delta * b # lowest demper

    # integrals
    xDotDot_1 = (F_mg_m1 + F_k0_m1 + F_b0_m1 - (F_k1_m1+F_b1_m1)) / m_1
    xDot_1 = xDot_1 + xDotDot_1 * t 
    x_1 = x_1 + xDot_1 * t

    """
        x_2
    """
    # level 1 deltas
    level_1_k_delta = x_2 - (x_1+h)
    level_1_b_delta = xDot_2 - xDot_1

    # level 2 deltas
    level_2_k_delta = h_0 - (x_2+h)
    level_2_b_delta = xDot_2


    F_mg_2 = -g*m_2
    # level 1
    F_k1_m2 = level_1_k_delta * k # lowest spring
    F_b1_m2 = level_1_b_delta * b # lowest demper
    # level 2
    F_k2_m2 = level_2_k_delta * k # lowest spring
    F_b2_m2 = level_2_b_delta * b # lowest demper


    # integrals
    xDotDot_2 = (F_mg_2 + F_k1_m2 + F_b1_m2 - (F_k2_m2 + F_b2_m2) ) / m_2
    xDot_2 = xDot_2 + xDotDot_2 * t 
    x_2 = x_2 + xDot_2 * t

    # save values
    t_values.append(t)
    x_1_values.append(x_1)
    xDot_1_values.append(xDot_1)
    xDotDot_1_values.append(xDotDot_1)
    x_2_values.append(x_2)
    xDot_2_values.append(xDot_2)
    xDotDot_2_values.append(xDotDot_2)

    # next step
    t += t_delta

plt.plot(t_values, x_1_values)
plt.plot(t_values, x_2_values)
plt.show()