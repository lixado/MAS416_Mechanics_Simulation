from math import floor
import os
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def animateFunction(points, seconds = 4, saveFolder = "./temp/", filename = "anime.mp4", fps = 150, number_points_draw = 10, expandedAxis = False):
    os.makedirs(saveFolder, exist_ok=True) # create folder if not exist 

    frames = fps*seconds
    print("FPS: ", fps)

    if len(points) < frames:
        raise "Wanted less frames then datapoints!"

    # split data into frames
    splitedList = split(points, frames)
    newPoints = []
    for chunck in splitedList:
        index = floor((len(chunck) - 1)/2)
        newPoints.append(chunck[index])

    x_values = [x for x,y in newPoints]
    y_values = [y for x,y in newPoints]

    fig = plt.figure()
    axis = plt.axes()
    if expandedAxis:
        axis = plt.axes(xlim =(round(min(x_values))-1, round(max(x_values))+1), ylim =(round(min(y_values)-1), round(max(y_values))+1))

    line, = axis.plot([], [], lw = 2)

    def init():
        line.set_data([], [])
        return line,

    # animation function
    def animate(i):
        line.set_data(x_values[i-number_points_draw:i], y_values[i-number_points_draw:i])
        return line,

    # calling the animation function	
    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = frames, interval = 20, blit = False)

    anim.save(saveFolder+filename + '.mp4', writer = 'ffmpeg', fps = fps)
    plt.close()

    