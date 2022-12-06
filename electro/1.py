import matplotlib.pyplot as plt


# constants
U0 = 0 # volts
U1 = 12 # volts
URampTime = 0.5 # seconds
R = 20 # ohm
L = 4 # henries
C = 2.5/1000 # mF -> Faraday

# state variables
i = 0
vU = 0
vR = 0
vC = 0

# time
t = 0
tDelta = 1e-4
tEnd = 3

# save arrays
I = []
VU = []
VR = []
VC = []
T = []


while t < tEnd:
    vU = U1 # initial voltage
    if t < URampTime:
        vU = (U1*t)/URampTime

    vR = vU - i * R # voltage after resistor

    iLDot = 1/L * (vR - vC) # current gradient in inductor
    vCDot = 1/C * i # voltage gradient in capacitor

    # integrate
    i = i + iLDot * tDelta
    vC = vC + vCDot * tDelta

    # save variables
    I.append(i)
    VU.append(vU)
    VR.append(vR)
    VC.append(vC)
    T.append(t)

    t += tDelta # update time


plt.plot(T, I)
plt.show()