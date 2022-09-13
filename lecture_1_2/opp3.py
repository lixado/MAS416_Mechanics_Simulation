from math import cos, pi, sin
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
    Variables
"""
os.makedirs("./opp3/", exist_ok=True)
L = 0.7 # meters    length
m = 24 # kg     mass
g = 9.81 # m/s**2

phi_start = pi/4# 45 degrees = pi/4 rad at t = 0
phi_derived_start = 2 # rad/sec at t = 0
t_start = 0

# range
func_start = 0
func_stop = 8

h = 1e-2 # step size

"""
    Functions
"""

# returns radiens of phi based on time

def phi_2nd_derived(prev_phi, g, L):
    return -( (g/L) * sin(prev_phi) )

phi_values = []
phi_derived_values = []
t_values = []

while t_start < func_stop:
    # calculate phi values
    phi_derived_n = phi_derived_start + h * phi_2nd_derived(phi_start, g, L) # calculate new y
    phi_n = phi_start + h * phi_derived_n
    phi_values.append(phi_n)
    phi_derived_values.append(phi_derived_n)
    
    # update t values
    t_start += h # add step size for new t
    t_values.append(t_start)

    # update phi values
    phi_start = phi_n
    phi_derived_start = phi_derived_n


"""
    Simulation of phi(t)
"""
fig = plt.figure()
axis = plt.axes(xlim =(func_start, func_stop),
				ylim =(min(phi_values), max(phi_values)))

line, = axis.plot([], [], lw = 2)

def init():
	line.set_data([], [])
	return line,

# animation function
def animate(i):
	line.set_data(t_values[0:i], phi_values[0:i])
	return line,

seconds = 8
frames = len(phi_values)
fps = int(frames/seconds)

# calling the animation function	
anim = animation.FuncAnimation(fig, animate,
							init_func = init,
							frames = int(abs(func_start-func_stop)/h),
							interval = h,
							blit = True)

# saves the animation in our desktop
anim.save('./opp3/phi_of_t.mp4', writer = 'ffmpeg', fps = fps)


"""
    Calculate position of every point
"""
x_values = []
y_values = []

for i,t in enumerate(t_values):
    x = sin(phi_values[i])* L
    y = -cos(phi_values[i])* L

    x_values.append(x)
    y_values.append(y)


"""
    Simulation of position
"""
seconds = 8
frames = len(y_values)
fps = int(frames/seconds)

fig = plt.figure()
axis = plt.axes(xlim =(round(min(x_values)), round(max(x_values))),
				ylim =(round(min(y_values)), round(max(y_values))))

line, = axis.plot([], [], lw = 2)

def init():
	line.set_data([], [])
	return line,

# animation function
def animate(i):
    number_points_draw = 10
    if i > number_points_draw:
        line.set_data(x_values[i-number_points_draw:i], y_values[i-number_points_draw:i])
    else:
        line.set_data(x_values[i-number_points_draw:i], y_values[i-number_points_draw:i])

    return line,

# calling the animation function	
anim = animation.FuncAnimation(fig, animate,
							init_func = init,
							frames = len(y_values), # h could be a problem not 
							interval = h,
							blit = True)

# saves the animation in our desktop
anim.save('./opp3/position_of_t.mp4', writer = 'ffmpeg', fps = fps)

