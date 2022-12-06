import matplotlib.pyplot as plt
from math import pi, sin, sqrt

# constants
R1 = 800
R2 = 1500
R3 = 1500
C1 = 9/1e6 # micro farad
C2 = 310/1e6
rampUp_t = 0.7
US1Max = 15

# state variables
vUs1 = 0
vC1 = 0
vC2 = 0
iR1 = 0
iR2 = 0
iR3 = 0

# time
t = 0
tDelta = 1e-4
tEnd = 3.8

# save arrays
T = []
IR1 = []
IR2 = []
IR3 = []
VC1 = []
VC2 = []


while t < tEnd:
    vUs1 = (US1Max / rampUp_t) * t
    if t > rampUp_t:
        vUs1 = US1Max

    iR1 = (US1Max - vC1) / R1
    iR2 = (vC1 - vC2) / R2
    i



    # integrate


    # save variables
    T.append(t)
    IR3.append(iR3)

    t += tDelta # update time


plt.plot(T, IR3)
plt.title(f'Abs(max): {max(abs(IR3))}')
plt.show()