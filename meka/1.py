import matplotlib.pyplot as plt
from math import pi, sin, sqrt
import numpy as np

# constants
p1_max = 150e5 # Maximum inlet pressure, Bar->Pa
Cd = 0.55 # Discharge coefficient
Ad = 3e-6 # Discharge area, mm^2->m^2
V2 = 2000e-6 # Size of volume 2, cm^3->m^3
beta = 9e8 # Bulk modulus 900 MPa -> 900e6 N/m^2 -> 9e8 N/m^2
rho = 850 # Liquid density, kg/m^3
pmin = -1e5 # Minimum gauge pressure, Bar->Pa
t_ramp = 0.3

# state variables
p2 = 0
p1 = 0

# time
t = 0
tDelta = 1e-4
tEnd = 0.5

# save arrays
T = []
P1 = []
P2 = []


while t < tEnd:
    p1 = p1_max
    if t < t_ramp:
        p1 = (p1_max/t_ramp) * t

    Q = Cd * Ad * np.sign(p1-p2) * ((2/rho) * abs(p1-p2))**0.5 # Compute volume flow
    p2Dot = (beta/V2) * Q # pressure gradient

    # integrate
    p2 += p2Dot * tDelta


    # save variables
    T.append(t)
    P1.append(p1)
    P2.append(p2)

    t += tDelta # update time


plt.plot(T, P1, label = "P1")
plt.plot(T, P2, label = "P2")
plt.legend()
plt.title(f'')
plt.show()