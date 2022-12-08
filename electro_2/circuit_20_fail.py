import matplotlib.pyplot as plt
from math import pi, sin, sqrt

# constants
R1 = 2400
R2 = 1600
R3 = 2200
R4 = 1600
C1 = 16/1e6
C2 = 8/1e6
C3 = 6/1e6
C4 = 18/1e6
L1 = 28
t_RU1 = 1.0
Us1_max = 24.0

# state variables
vC1 = 0
vC2 = 0
vC3 = 0
vC4 = 0
iL1 = 0

# time
t = 0
tDelta = 1e-4
tEnd = 3

# save arrays
T = []
IL1 = []


while t < tEnd:
    vUs1 = (Us1_max / t_RU1) * t
    if t >= t_RU1:
        vUs1 = Us1_max
    
    iR1 = (vUs1 - vC1) / R1
    iR2 = (vC1 - vC2) / R2
    iR3 = (vC2 - vC3) / R3
    iR4 = (vC3 - vC4) / R4
    iL1Dot = 1/L1 * (vUs1 - vC4)
    vC1Dot = 1/C1 * (iR1 - iR2)
    vC2Dot = 1/C2 * (iR2 - iR3)
    vC3Dot = 1/C3 * (iR3 - iR4)
    vC4Dot = 1/C4 * (iR4 + iL1)

    # integrate
    iL1 += iL1Dot * tDelta
    vC1 += vC1Dot * tDelta
    vC2 += vC2Dot * tDelta
    vC3 += vC3Dot * tDelta
    vC4 += vC4Dot * tDelta

    # save variables
    T.append(t)
    IL1.append(iL1 * 1000)

    t += tDelta # update time


plt.plot(T, IL1)
plt.title(f'RMS: { max(IL1) / sqrt(2) }')
plt.show()


# 0,4495 (med marginen: 0,009)