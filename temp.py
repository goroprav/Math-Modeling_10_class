import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

import numpy as np

fig=plt.figure()
ax=p3.Axes3D(fig)
t=np.linspace(0,2*np.pi,100)
F=np.linspace(0,2*np.pi,100)
R=1
a=1
b=1
c=1
x=a*np.outer(np.cos(F), np.sinh(t))
y=b*np.outer( np.sin(F), np.sinh(t))
z=c*np.outer(np.ones(np.size(F)), np.sinh(t))

ax.plot_surface(x,y,z, color='g')

a=1
b=1
c=-1
x=a*np.outer(np.cos(F), np.sinh(t))
y=b*np.outer( np.sin(F), np.sinh(t))
z=c*np.outer(np.ones(np.size(F)), np.sinh(t))

ax.plot_surface(x,y,z, color='g')

plt.show()

