import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D

points  = np.array([
	[-1,2,1],
	[3,4,3]])

# Create the figure
fig = plt.figure()

# Add an axes
ax = fig.add_subplot(111,projection='3d')

# plot the surface
#ax.add_line(Line3D(*points))
#ax.add_line(points[0],points[1])
ax.plot(*zip(*points))
#ax.plot([points[0][0],points[1][0]], [points[0][1],points[1][1]],[points[0][2],points[1][2]])

# and plot the point
for point in points:
	ax.scatter(*point)

plt.show()
