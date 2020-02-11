import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

import numpy as np

fig=plt.figure()
ax=p3.Axes3D(fig)
t=np.linspace(0,2*np.pi,100)
F=np.linspace(0,2*np.pi,100)
l=0.5
m=3
n=10

x=np.outer(F, np.cos(t))+l*np.outer(np.ones(np.size(F)), t**2)
y=np.outer(F, np.sin(t))+m*np.outer(np.ones(np.size(F)), t**2)
z=n*np.outer( np.ones(np.size(F)),t**0.5)

ax.plot_surface(x,y,z, color='g')

plt.show()

