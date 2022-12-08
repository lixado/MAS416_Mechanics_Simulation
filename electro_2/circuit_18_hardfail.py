import matplotlib.pyplot as plt
from math import pi, sin, sqrt

# constants
R1 = 1600
R2 = R1
R3 = 1800
R4 = R3
C1 = 10/1e6
C2 = 12/1e6
C3 = 8/1e6
L1 = 20
L2 = 26
t_RU1 = 0.9
Us1_max = 12

# state variables
vC1 = 0
vC2 = 0
vC3 = 0
iL1 = 0
iL2 = 0

# time
t = 0
tDelta = 1e-4
tEnd = 2.9

# save arrays
T = []
IR3 = []


while t < tEnd:
    vUs1 = (Us1_max / t_RU1) * t
    if t >= t_RU1:
        vUs1 = Us1_max

    vL1 = R1 * iL1 # U = R*I
    iR1 = (vUs1 - vL1) / R1

    iR3 = (vL1 - vC1) / R3
    
    vL2 = R2 * iL2
    iR2 = (vL1 - vL2) / R2

    iR4 = (vL1 - vC3) / R3
    

    vC1Dot = 1/C1 * (iR3)
    vC2Dot = 1/C2 * (iR1 - iR2 - iR3 - iR4)
    vC3Dot = 1/C3 * (iR2 + iR4)
    iL1Dot = 1/L1 * (vUs1 - vC2)
    iL2Dot = 1/L2 * (vC2 - vC3)

    # integrate
    vC1 += vC1Dot*tDelta
    vC2 += vC2Dot*tDelta
    vC3 += vC3Dot*tDelta
    iL1 += iL1Dot*tDelta
    iL2 += iL2Dot*tDelta

    # save variables
    T.append(t)
    IR3.append(iR3 * 1000)

    t += tDelta # update time


plt.plot(T, IR3)
plt.title(f'Abs(max): {max([abs(x) for x in IR3])}')
plt.show()


# 0,1333 (med marginen: 0,0027)