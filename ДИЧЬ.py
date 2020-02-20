import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
n=0.1


R=1
N=200
t=np.linspace(0, 10, N)
R=1
g=9.81

def difu(s,t):
    x,v_x,y,v_y,z,v_z=s
    dxdt=v_x
    dv_xdt=3*g*z/(z**2+x**2)*x
    dydt=v_y
    dv_ydt=0
    dzdt=v_z
    dv_zdt=-g + 3*g*z/(z**2+x**2)*z
    return dxdt,dv_xdt,dydt,dv_ydt,dzdt,dv_zdt

x0=1
v_x0=0

y0=0
v_y0=1

z0=0
v_z0=0

s0=(x0,v_x0,y0,v_y0,z0,v_z0)
#Рисование плоскости




sol=odeint(difu,s0,t)

fig=plt.figure()
ax=p3.Axes3D(fig)

ball,=ax.plot(sol[:,0],sol[:,2],sol[:,4], 'o', color='b')
line,=ax.plot(sol[:,0],sol[:,2],sol[:,4], '-', color='b')
def anim(i):
    ball.set_data(sol[i,0],sol[i,2])
    ball.set_3d_properties(sol[i,4])
    
    line.set_data(sol[:i,0],sol[:i,2])
    line.set_3d_properties(sol[:i,4])
    
ani=animation.FuncAnimation(fig,anim,N,interval=50)

y=np.linspace(0,np.pi,100)
F=np.linspace(0,-np.pi,100)
R=1

x=R*np.outer(np.ones(np.size(t)), np.cos(F))
y=np.outer(t, np.ones(np.size(F)))
z=R*np.outer(np.ones(np.size(t)), np.sin(F))
ax.plot_surface(x,y,z, color='g')

plt.show()

ani.save('DICH.gif')
