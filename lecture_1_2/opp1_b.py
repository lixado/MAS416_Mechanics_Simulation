from matplotlib.pyplot import plot, show


def y(t):
    B = 0 # else
    if (t <= 2):
        B = 1-t

    return 1 * (t**2) + B

start = 0
stop = 15
step = 0.0001

t_values = []
y_values = []

y_start = y(start)
while y_start <= 10:
    t_values.append(start)
    y_values.append(y_start)

    start += step
    y_start = y(start)

plot(t_values, y_values)
show()