from math import sqrt
from matplotlib.pyplot import plot, show


y_start = 0
y_derived_start = 0
t_start = 0

# range
func_start = 0
func_stop = 1

h = 1e-5
print('h = {0:.16f}'.format(h))

def y_2nd_derived(t, y_derived, y):
    return 100 * (3-y) - 12 * y_derived

y_values = []
y_derived_values = []
t_values = []

while t_start < func_stop:
    y_derived_n = y_derived_start + h * y_2nd_derived(t_start, y_derived_start, y_start) # calculate new y
    y_n = y_start + h * y_derived_n
    y_values.append(y_n)
    y_derived_values.append(y_derived_n)

    t_start += h # add step size for new t
    t_values.append(t_start)

    y_start = y_n
    y_derived_start = y_derived_n


def f_of(t):
    val =  min(t_values, key=lambda x:abs(x-t))
    index = t_values.index(val)
    return y_values[index]

print("Print f(0.5)")
print(f_of(0.5))

plot(t_values, y_values)

print("Max y(t):", max(y_values))
print("Max y'(t):", max(y_derived_values))

squared_list = [x**2 for x in y_values]
rms = sqrt((1/len(y_values)) * sum(squared_list))
print("Root mean square y(t): ", rms)

rms = sqrt((1/len(y_values)) * sum([x**2 for x in y_derived_values]))
print("Root mean square y'(t): ", rms)

show()
