from math import pi, sin, cos, tanh
import matplotlib.pyplot as plt

"""
    Constants
"""
A = 0.2 # m
B = 0.1 # m/s
L_0 = 0.1 # 100 mm / 1000 = 0.1 m
k = 1000 # N/m
m = 300 # kg
g = 9.81 # m/s**2
theta = pi/6 # 30 degrees = pi/6

"""
    Variables
"""
x = 0.1 # 100 mm to m = 0.1 m
xDot = 0 # m/s
t_start = 0
t_end = 25 # s
t_delta = 0.001

F_0 = 500 # N
v_0 = 0.01 # m/s

t_values = []
x_values = []
xDot_values = []
xDotDot_values = []
while t_start < t_end:
    """
        Calculate new values
    """
    # F_fr force of friction
    F_fr = F_0*tanh(xDot / v_0)

    # F_k force of spring
    x_0 = A + B * t_start # x_0
    delta = x_0 - x - L_0
    F_k = 0 if delta < 0 else delta*k

    # F_mg force of gravity
    F_mg = sin(theta)*m*g
    

    # Integrals
    xDotDot = (F_k + F_fr - F_mg) / m
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


plt.plot(t_values, x_values)
plt.show()
