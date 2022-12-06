import matplotlib.pyplot as plt


# constants
R1, R2 = 200, 200 # ohm
C = 60/1e6 # microFaraday to Faraday
U1 = 12 # volts
UMax_t = 0.3 # seconds

# state variables
i1 = 0
i2 = 0
vU = 0
vC = 24

# time
t = 0
tDelta = 1e-5
tEnd = 0.5

# save arrays
I1 = []
I2 = []
VU = []
VC = []
T = []

while t < tEnd:
    vU = (U1/UMax_t) * t # voltage at start
    if t >= UMax_t:
        vU = U1

    # state variables
    i1 = vU / R1
    i2 = (vU - vC) / R2
    vCDot = 1/C * i2 # voltage gradient in capacitor

    # integrate
    vC = vC + vCDot*tDelta

    # save variables
    I1.append(i1)
    I2.append(i2)
    VU.append(vU)
    VC.append(vC)
    T.append(t)

    t += tDelta # update time


plt.plot(T, I1, label = "i1")
plt.plot(T, I2, label = "i2")
plt.legend()
plt.show()