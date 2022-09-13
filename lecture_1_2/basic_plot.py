from matplotlib.pyplot import plot, show


y_start = 1
t_start = 0

# range
func_start = 0
func_stop = 3

h = 1e-5
print('h = {0:.16f}'.format(h))

def y_derived(t, y):
    return -2 * y * t

y_values = []
t_values = []

while t_start < func_stop:
    y_n = y_start + h * y_derived(t_start, y_start) # calculate new y
    y_values.append(y_n)

    t_start += h # add step size for new t
    t_values.append(t_start)

    y_start = y_n


def f_of(t):
    val =  min(t_values, key=lambda x:abs(x-t))
    index = t_values.index(val)
    return y_values[index]

print("Print f(1)")
print(f_of(1))

plot(t_values, y_values)
show()
