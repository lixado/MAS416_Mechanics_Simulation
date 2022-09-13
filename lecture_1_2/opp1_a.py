from math import pi, sin, sqrt
from matplotlib.pyplot import plot, show


def y(t):
    A = 3 # else
    if (t <= 5):
        A = 1
    if (t > 5 and t <= 10):
        A = 2
    f = 0.5

    return A * sin(2 * pi * f * t)

start = 0
stop = 15
steps = 1000

t_values = [x/steps for x in range(start, stop*steps)]
y_values = [y(x) for x in t_values]

plot(t_values, y_values)
show()


print("Max:", max(y_values))

squared_list = [x**2 for x in y_values]
rms = sqrt((1/len(y_values)) * sum(squared_list))
print("Root mean square: ", rms)
