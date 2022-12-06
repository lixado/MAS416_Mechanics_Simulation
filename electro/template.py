import matplotlib.pyplot as plt
from math import pi, sin, sqrt

# constants


# state variables


# time
t = 0
tDelta = 1e-4
tEnd = 3

# save arrays
T = []


while t < tEnd:


    # integrate


    # save variables
    T.append(t)

    t += tDelta # update time


plt.plot(T, )
plt.show()