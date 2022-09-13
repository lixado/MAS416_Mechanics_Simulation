import os
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def animateFunction(points, delta_t, seconds = 4, saveFolder = "./temp/"):
    os.makedirs(saveFolder, exist_ok=True) # create folder if not exist 

    frames = len(points)
    fps = int(frames/seconds)
    print("FPS: ", fps)

    x_values = [x for x,y in points]
    y_values = [y for x,y in points]

    fig = plt.figure()
    axis = plt.axes(xlim =(round(min(x_values))-1, round(max(x_values))+1),
                    ylim =(round(min(y_values))-1, round(max(y_values))+1))

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
                                frames = frames, # h could be a problem not 
                                interval = delta_t,
                                blit = True)

    anim.save(saveFolder+'/anime.mp4', writer = 'ffmpeg', fps = fps)

    