from skspatial.objects import Line, Points
from skspatial.plotting import plot_3d
import matplotlib.pyplot as plt

points = Points(
    [
        [2, 0.5, 1.6], 
        [2, -0.5, 1.6], 
        [1.6, 0.5, 0.9], 
        [1.6, 0, 0.9]
    ],
)

line_fit = Line.best_fit(points)


plot_3d(
    line_fit.plotter(t_1=-7, t_2=7, c='k'),
    points.plotter(c='b', depthshade=False),
)

plt.show()