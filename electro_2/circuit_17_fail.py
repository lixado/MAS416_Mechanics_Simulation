import matplotlib.pyplot as plt
from math import pi, sin, sqrt

# constants
R1 = 2400
R2 = 1400
R3 = 2200
C1 = 18/1e6 # micro farad to farad
C2 = 17/1e6
C3 = 8/1e6
L1 = 24
L2 = 20
t_RU_1 = 0.3
Us1_max = 14

# state variables
vC1 = 0
vC2 = 0
vC3 = 0
iL1 = 0
iL2 = 0
iR1 = 0

# time
t = 0
tDelta = 1e-4
tEnd = 2.6

# save arrays
T = []
IR1 = []


while t < tEnd:
    vUs1 = (Us1_max / t_RU_1) * t
    if t >= t_RU_1:
        vUs1 = Us1_max

    iR1 = (vUs1 - vC1) / R1
    iR2 = (vC1 - vC2) / R2
    iR3 = (vC2 - vC3) / R3
    iL1Dot = 1/L1 * (vC1 - vC3)
    iL2Dot = 1/L2 * (vC1)
    vC1Dot = 1/C1 * (iL1 - iR2)
    vC2Dot = 1/C2 * (iR2 - iR3)
    vC3Dot = 1/C3 * (iL2 + iR3)

    # integrate
    iL1 += iL1Dot*tDelta
    iL2 += iL2Dot*tDelta
    vC1 += vC1Dot*tDelta
    vC2 += vC2Dot*tDelta
    vC3 += vC3Dot*tDelta


    # save variables
    T.append(t)
    IR1.append(iR1 * 1000)

    t += tDelta # update time


plt.plot(T, IR1)
plt.title(f'Abs(max): {max([abs(x) for x in IR1])}')
plt.show()

# 0,7311 (med marginen: 0,0146)