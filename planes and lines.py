import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
#from mayavi import mlab

points = np.array([
	[-1,2,1],
	[3,4,3]])

# Create the figure
fig = plt.figure()

# Add an axes
#ax = fig.add_subplot(111,projection='3d')
ax = fig.gca(projection='3d')

# plot line
#ax.add_line(Line3D(*points))
#ax.add_line(points[0],points[1])
ax.plot(*zip(*points))
#ax.plot([points[0][0],points[1][0]], [points[0][1],points[1][1]],[points[0][2],points[1][2]])

# plot surface
planes = np.array([
	[1,-3,1,6],
	[4,-6,1,12]])

for plane in planes:
	a,b,c,d = plane
	X,Y = np.meshgrid(range(6),range(6))
	Z = (d - a*X - b*Y) / c
	ax.plot_surface(X, Y, Z, alpha=.2)
	#mlab.mesh(X, Y, Z)

# plot line
points = np.array([
	[0,2,0],
	[1/2,1/2,1]])
ax.plot(*zip(*points))

# and plot the point
for point in points:
	ax.scatter(*point)

plt.show()
#mlab.show()