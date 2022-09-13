from math import pi, sin, cos
import matplotlib.pyplot as plt
from animation import animateFunction

"""
    Constants
"""
J = 2 # kg m**2
k_0 = 1800 # N*m / rad
b_0 = 8 # N*m*s / rad
t_end = 4

def simulation(M_0, omega_p, t_interval = 0.0001):
    """
        Variables
    """
    t_start = 0
    theta = (5*pi)/36 # degrees = 25 degrees
    thetaDot = 0 # rad/s

    t_values = []
    theta_values = []
    thetaDot_values = []
    thetaDotDot_values = []

    while t_start < t_end:
        # Deltas
        delta_theta = theta
        #if len(theta_values) > 0:
        #    delta_theta -= theta_values[-1] WHYYY NOT???

        delta_thetaDot = thetaDot
        #if len(thetaDot_values) > 0:
        #    delta_thetaDot -= thetaDot_values[-1] WHY?????


        # Forces
        m_t = M_0 * sin(t_start * omega_p) # M(t)
        m_k = k_0*(delta_theta) # k_0*(delta_theta - beta_0) WHY NO BETA?
        m_b = b_0*(delta_thetaDot)

        # Integrals
        thetaDotDot = (m_t - m_k - m_b) / J
        thetaDot = thetaDot + t_interval * thetaDotDot
        theta = theta + t_interval * thetaDot

        # save results
        t_values.append(t_start)
        theta_values.append(theta)
        thetaDot_values.append(thetaDot)
        thetaDotDot_values.append(thetaDotDot)

        # next step
        t_start += t_interval

    return t_values, theta_values, thetaDot_values, thetaDotDot_values

"""
    Plots
"""
fig, axs = plt.subplots(2, 2)
fig.suptitle("Simulations")

# a)
t_values, theta_values, thetaDot_values, thetaDotDot_values = simulation(0, 0)
axs[0, 0].plot(t_values, theta_values)
axs[0, 0].set_title(f'Simulation a) 0, 0')
xy_points = [(cos(theta), sin(theta)) for theta in theta_values]
animateFunction(xy_points, t_end, "./lecture_1_2/opp5/", "a", expandedAxis=True)

# b)
t_values, theta_values, thetaDot_values, thetaDotDot_values = simulation(75, 20)
axs[0, 1].plot(t_values, theta_values)
axs[0, 1].set_title(f'Simulation b) 75, 20')
xy_points = [(cos(theta), sin(theta)) for theta in theta_values]
animateFunction(xy_points, t_end, "./lecture_1_2/opp5/", "b", expandedAxis=True)

# c)
t_values, theta_values, thetaDot_values, thetaDotDot_values = simulation(75, 30)
axs[1, 0].plot(t_values, theta_values)
axs[1, 0].set_title(f'Simulation c) 75, 30')
xy_points = [(cos(theta), sin(theta)) for theta in theta_values]
animateFunction(xy_points, t_end, "./lecture_1_2/opp5/", "c", expandedAxis=True)

# d)
t_values, theta_values, thetaDot_values, thetaDotDot_values = simulation(75, 40)
axs[1, 1].plot(t_values, theta_values)
axs[1, 1].set_title(f'Simulation d) 75, 40')
xy_points = [(cos(theta), sin(theta)) for theta in theta_values]
animateFunction(xy_points, t_end, "./lecture_1_2/opp5/", "d", expandedAxis=True)


plt.show()
