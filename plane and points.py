import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

points  = np.array([
	[1, 1, -1],
	[2,0,2],
	[5,0,2]])
normal = np.array([0, 9, 3])

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate d and we're set
d = -points[1].dot(normal)

# create x,y
xx, yy = np.meshgrid(range(6), range(6))

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

# plot the surface
#plt3d = plt.figure().gca(projection='3d')
#plt3d.plot_surface(xx, yy, z, alpha=0.2)

#and i would like to plot this point : 
#ax.scatter(point2[0] , point2[1] , point2[2],  color='green')

# Create the figure
fig = plt.figure()

# Add an axes
ax = fig.add_subplot(111,projection='3d')

# plot the surface
ax.plot_surface(xx, yy, z, alpha=0.2)

# and plot the point
for point in points:
	ax.scatter(point[0] , point[1] , point[2],  color='green')

plt.show()