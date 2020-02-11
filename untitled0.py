import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

import numpy as np

fig=plt.figure()
ax=p3.Axes3D(fig)
t=np.linspace(0,2*np.pi,100)
F=np.linspace(0,2*np.pi,100)
R=1

x=np.outer(t, np.cos(F))
y=np.outer(t, np.sin(F) )
z=np.outer(t**2, np.ones(np.size(F)))

ax.plot_surface(x,y,z, color='g')

plt.show()

