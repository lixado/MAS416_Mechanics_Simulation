import matplotlib.pyplot as plt
from math import pi, sin, sqrt
import numpy as np

# constants
rho = 875 # kg/m^3
beta = 1100* 1e6 # MPa mega pascal to Pa
pmin = -1 * 1e5 # Bar to Pa
Qs01 = 53 * 6e-4 # L/min
V1 = 637 * 1e-6 # cm**3 to m**3
V2 = 799 * 1e-6 # cm**3 to m**3
V3 = 463 * 1e-6 # cm**3 to m**3
V4 = 989 * 1e-6 # cm**3 to m**3
Cd1 = 0.71
Cd2 = 0.55
Cd3 = 0.65
Cd4 = 0.48
Cd5 = 0.49
Cd6 = 0.67
Ad1 = 39 * 1e-6 # mm**2 to m**2
Ad2 = 38 * 1e-6
Ad3 = 25 * 1e-6
Ad5 = 40 * 1e-6
Ad6 = 36 * 1e-6
t_RU1 = 153 * 1e-3 # ms to s

# state variables
p1 = 0
p2 = 0
p3 = 0
p4 = 0

# time
t = 0
tDelta = 1e-4
tEnd = 306 * 1e-3 # ms to s

# save arrays
T = []
P3 = []


while t < tEnd:
    Qs1 = (Qs01 / t_RU1) * t
    if t > t_RU1:
        Qs1 = Qs01

    # p2dot is a given
    p2Dot = (beta/V2) * Qs1 

    # now to calculate p1dot
    Q2 = Cd2 * Ad2 * np.sign(pmin-p1) * sqrt((2/rho) * abs(pmin-p1)) # Compute volume flow
    Q1 = Cd1 * Ad1 * np.sign(p1-p3) * sqrt((2/rho) * abs(p1-p3))
    p1Dot = (beta/V1) * (Q2 - Q1) # pressure gradient

    # now to calculate p3dot we need Q1 Q3 and Q5
    Q3 = Cd3 * Ad3 * np.sign(p3-pmin) * sqrt((2/rho) * abs(p3-pmin))
    Q5 = Cd5 * Ad5 * np.sign(p3-p4) * sqrt((2/rho) * abs(p3-p4))
    p3Dot = (beta/V3) * (Q1 - Q3 - Q5)

    # now to calculate p4Dot we need Q6
    Q6 = Cd6 * Ad6 * np.sign(p4-0) * sqrt((2/rho) * abs(p4-0))
    p4Dot = (beta/V4) * (Q5 - Q6)   

    
    # integrate
    p1 += p1Dot*tDelta
    p2 += p2Dot*tDelta
    p3 += p3Dot*tDelta
    p4 += p4Dot*tDelta


    # save variables
    T.append(t)
    P3.append(p3 * 1e-5)

    t += tDelta # update time


plt.plot(T, P3)
plt.title(f'Abs(max): {max([abs(x) for x in P3])}') # i got 2.327
plt.show()

# 2,823 (med marginen: 0,0565)