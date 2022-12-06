import matplotlib.pyplot as plt
from math import pi, sin, sqrt

# constants
R1 = 200
R2 = R1
Us1Max = 10
Us1Start = 0
Us1Max_time = 1
C1 = 60/1e6 # microFaraday -> faraday
C2 = 50/1e6 # microFaraday -> faraday

# state variables
iR1 = 0
iR2 = 0
vC1 = 10
vC2 = vC1

# time
t = 0
tDelta = 1e-4
tEnd = 3

# save arrays
T = []


while t < tEnd:
    vUs1 = (Us1Max / Us1Max_time) * t
    if t >= Us1Max_time:
        vUs1 = Us1Max

    # U = R*I
    iR1 = vUs1 / R1
    iR2 = vUs1 / R2


    # integrate


    # save variables
    T.append(t)

    t += tDelta # update time


plt.plot(T, )
plt.show()