from math import pi, sin, sqrt
import matplotlib.pyplot as plt


# constants
R = 1500 # ohm
C = 60/1e6 # microFaraday -> faraday
V1 = 120 # volt
f1 = 50 # Hz
RD = 1 # ohm

# state variables
iD = 0
iR = 0
vC = 0 # volt
vUs1 = 0

# time
t = 0
tDelta = 1e-5
tEnd = 0.1

# save arrays
T = []
I1 = []
I2 = []
VUS1 = []
VC = []

while t < tEnd:
    vUs1 = sqrt(2) * V1 * sin(2 * pi * f1 * t)

    # state variables
    iD = 0
    if vUs1 > vC:
        iD = (vUs1 - vC)/RD

    iR = vC / R
    vCDot = 1/C * (iD - iR)

    # integrate
    vC = vC + vCDot*tDelta

    # save variables
    VUS1.append(vUs1)
    VC.append(vC)
    T.append(t)

    t += tDelta # update time

plt.plot(T, VUS1, label = "VUS1")
plt.plot(T, VC, label = "VC")
plt.legend()
plt.show()