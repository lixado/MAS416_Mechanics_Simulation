from math import pi, sin, sqrt
import matplotlib.pyplot as plt


# constants
R1 = 5000
R2 = 2000
R3 = 1200
R4 = 8000
R5 = R3
C1 = 380/1e6
C2 = C1
L1 = 50
Us1Min = 60
Us1Start = 120
Us1Min_time = 1

# state variables
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
vUs1 = 0
vUs2 = 120 # constant
vC1 = 60
vC2 = vC1

# time
t = 0
tDelta = 1e-5
tEnd = 6

# save arrays
T = []
I1 = []
I2 = []
I3 = []
I4 = []
I5 = []
VUS1 = []
VUS2 = []
VC1 = []
VC2 = []

while t < tEnd:
    vUs1 = Us1Start - Us1Min/1 * t
    if t >= Us1Min_time:
        vUs1 = Us1Min

    # state variables
    i1 = (vUs2 - vUs1) / R1
    i3 = (vUs1 - vC1) / R3
    i4 = (vUs1 - vC1) / R4
    i5 = (vC1 - vC2) / R5
    iC1 = i3 + i4 - i5 # 0 = i3 + i4 - i5 - iC1 kirchkoffs
    vL1 = i2 * R2 # U = RI ohms

    i2Dot = 1/L1 * (vUs1 - vL1)
    vC1Dot = 1/C1 * iC1
    vC2Dot = 1/C2 * i5

    # integrate
    i2 += i2Dot*tDelta
    vC1 += vC1Dot*tDelta
    vC2 += vC2Dot*tDelta

    # save variables
    I1.append(i1)
    I2.append(i2)
    I3.append(i3)
    I4.append(i4)
    I5.append(i5)
    T.append(t)

    t += tDelta # update time

plt.plot(T, I1, label = "I1")
plt.plot(T, I2, label = "I2")
plt.plot(T, I3, label = "I3")
plt.plot(T, I4, label = "I4")
plt.plot(T, I5, label = "I5")
plt.legend()
plt.show()