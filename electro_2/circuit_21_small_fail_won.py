import matplotlib.pyplot as plt
from math import pi, sin, sqrt

# constants
R1 = 2200
R2 = 1800
R3 = 2000
C1 = 7/1e6
C2 = 19/1e6
RD1 = 1
V1 = 100
f1 = 50

# state variables
vC1 = 0
vC2 = 0

# time
t = 0
tDelta = 1e-7
tEnd = 0.08

# save arrays
T = []
IR1 = []

while t < tEnd:
    vUs1 = sqrt(2) * V1 * sin(2*pi*f1*t)

    iD = 0
    if vC1 > vC2:
        iD = (vC1 - vC2)/RD1

    iR1 = (vUs1 - vC1) / R1
    iR2 = (vUs1 - vC2) / R2
    iR3 = vC2/R3 # U = R*I
    vC1Dot = 1/C1 * (iR1 - iD)
    vC2Dot = 1/C2 * (iD + iR2 - iR3)

    # integrate
    vC1 += vC1Dot*tDelta
    vC2 += vC2Dot*tDelta


    # save variables
    T.append(t)
    IR1.append(iR1 * 1000)

    t += tDelta # update time


plt.plot(T, IR1)
plt.title(f'RMS: { max(IR1) / sqrt(2) }')
plt.show()