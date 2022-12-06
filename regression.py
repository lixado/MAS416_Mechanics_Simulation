import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize

# x,y,z
points = np.array(
        [[2, 0.5, 1.6], 
        [2, -0.5, 1.6], 
        [1.6, 0.5, 0.9], 
        [1.6, 0, 0.9]])

xData = points[:, 0]
yData = points[:, 1]
zData = points[:, 2]

data = [xData, yData, zData]


#Plotting
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')





print("y: ", yData)

ax.scatter(xData, yData, zData)

plt.show()
