from math import pi, sin, cos, tanh
import matplotlib.pyplot as plt

"""
    Constants
"""
A = 0.2 # m
B = 0.1 # m/s
L_0 = 100/1000 # 100 mm * 1000 = 0.1 m
k = 1000 # N/m
m = 300 # kg
g = 9.81 # m/s**2

def F_k(t, A, B, x, L_0):
    x_t = A+B*t
    delta = x_t - x - L_0

    if delta >= 0:
        return k*delta
    else:
        return 0

def F_fr(xDot, F_start, v_0):
    return F_start * tanh(xDot / v_0)

def F_mg(theta, g, m):
    return sin(theta)*m*g


"""
    Variables
"""
F_0 = 500 # N
v_0 = 0.01 # m/s
x = 100/1000 # 100 mm to m = 0.1 m
xDot = 0 # m/s
theta = pi/6 # 30 degrees = pi/6
t_start = 0
t_end = 25 # s
t_delta = 0.001

t_values = []
x_values = []
xDot_values = []
xDotDot_values = []
while t_start < t_end:
    """
        Calculate new values
    """

    # Integrals
    xDotDot = (1/m)*(F-G-D-S)
    xDot = xDot + t_delta * xDotDot
    x = x + t_delta * xDot
    
    """
        Record values
    """
    xDotDot_values.append(xDotDot)
    xDot_values.append(xDot)
    x_values.append(x)
    t_values.append(t_start)

    """
        Update values
    """
    t_start += t_delta # next t




