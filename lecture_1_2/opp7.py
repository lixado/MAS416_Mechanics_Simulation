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

t_values = []
x_1_values = []
xDot_1_values = []
xDotDot_1_values = []

x_2_values = []
xDot_2_values = []
xDotDot_2_values = []

while t < t_end:
    """
        x_1
    """
    


    """
        x_2
    """

    # next step
    t += t_delta