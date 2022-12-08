import matplotlib.pyplot as plt
from math import pi, sin, sqrt

# constants
R1 = 1100
R2 = 1300
R3 = 1600
R4 = 500
R5 = 1700
R6 = 700
R7 = 1200
C1 = 45/1e6
C2 = 45/1e6
t_RU1 = 0.3
Us1_max = 19
t_RU2 = 0.3
Us2_max = 14

# state variables
vC1 = 0
vC2 = 0

# time
t = 0
tDelta = 1e-5
tEnd = 3.4

# save arrays
T = []
IR4 = []

while t < tEnd:
    vUs1 = (Us1_max / t_RU1) * t
    if t >= t_RU1:
        vUs1 = Us1_max

    vUs2 = (Us2_max / t_RU2) * t
    if t >= t_RU2:
        vUs2 = Us2_max

    iR1 = (vUs1 - vC1) / R1
    iR2 = (vC1 - vC2) / R2
    iR3 = (vC1 - vUs2) / R3
    iR4 = (vC1 - vC2) / R4 
    iR5 = (vC2 - vUs2) / R5
    iR6 = (vUs2 - vUs1) / R6
    iR7 = (vUs1) / R7
    vC1Dot = 1/C1 * (iR1 - iR4 - iR2 - iR3)
    vC2Dot = 1/C2 * (iR4 + iR2 - iR5)

    # integrate
    vC1 += vC1Dot * tDelta
    vC2 += vC2Dot * tDelta


    # save variables
    T.append(t)
    IR4.append(iR4 * 1000)

    t += tDelta # update time


plt.plot(T, IR4)
plt.title(f'RMS: { max(IR4) / sqrt(2) }')
plt.show()

#0,8225 (med marginen: 0,0164)