import matplotlib.pyplot as plt
from math import pi, sin, sqrt

# constants
R1 = 3200
L1 = 66
C1 = 145/1e6 # microfarad -> farad
V1 = 230
f1 = 50 # Hz

# state variables
vC1 = 0
iL1 = 0
iR1 = 0 

# time
t = 0
tDelta = 1e-4
tEnd = 0.08

# save arrays
T = []
IR1 = []
VUS1 = []

while t < tEnd:
    vUs1 = sqrt(2) * V1 * sin(2 * pi * f1 * t)

    iR1 = (vUs1 - vC1) / R1
    iL1Dot = 1/L1 * (vUs1 - vC1)
    vC1Dot = 1/C1 * (iR1 + iL1)

    # integrate
    iL1 += iL1Dot*tDelta
    vC1 += vC1Dot*tDelta

    # save variables
    T.append(t)
    IR1.append(iR1 * 1000) # turn to mili ampere
    VUS1.append(vUs1)

    t += tDelta # update time

plt.plot(T, IR1) # in miliAmpere
plt.title(f'RMS: { max(IR1) / sqrt(2) }')
plt.show()