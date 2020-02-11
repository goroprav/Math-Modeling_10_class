import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
#from matplotlib import animation
import numpy as np

fig=plt.figure()
ax=p3.Axes3D(fig)
t=np.linspace(0,2*np.pi,100)
F=np.linspace(0,2*np.pi,500)
#N=100
#A=np.linspace(2*np.pi,0,N)
#y=np.sin(A)
#z=A*0.1
#ball,= ax.plot(x,y,z, 'o', color='b')
#line,= ax.plot(x,y,z, '-', color='b')

x1=np.outer(np.cos(t), F)
y1=np.outer(np.sin(t),F)
z1=h*np.outer(F**0.5,np.ones(np.size(F)))
#def func(i):
   # ball.set_data(x[i],y[i])
 #   ball.set_3d_properties(z[i])
  #  line.set_data(x[:i], y[:i])  
 #   line.set_3d_properties(z[:i])
    
#ax.set_xlim3d([-1.0,1.0])
#ax.set_ylim3d([-1.0,1.0])
#ax.set_zlim3d([-1.0,1.0])    
ax.plot_surface(x1,y1,z1, color='g')
#ani= animation.FuncAnimation(fig,func,N, interval=50)
#ani.save('ani.gif')
