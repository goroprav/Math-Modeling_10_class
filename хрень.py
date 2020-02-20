import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

N=200
t=np.linspace(0, 1, N)
a=3
b=2
c=2
g=9.81

def func(s,t):
    x,v_x,y,v_y,z,v_z = s
    
    dxdt=v_x
    dv_xdt=(x/a**2)* (g-(v_x**2/a**2)-(v_y**2/b**2)-(v_z**2/c**2))/((x**2/a**4)+(y**2/b**4)+(z**2/b**4))
    
    dydt=v_y
    dv_ydt=(y/b**2)* (g-(v_x**2/a**2)-(v_y**2/b**2)-(v_z**2/c**2))/((x**2/a**4)+(y**2/b**4)+(z**2/b**4))
    
    dzdt=v_z
    dv_zdt=-g+(x/a**2)*(g-(v_x**2/a**2)-(v_y**2/b**2)-(v_z**2/c**2))/((x**2/a**4)+(y**2/b**4)+(z**2/b**4))
    
    return dxdt,dv_xdt,dydt,dv_ydt,dzdt,dv_zdt

x0=0
v_x0=0

y0=0
v_y0=0

z0=3
v_z0=0

s0=(x0,v_x0,y0,v_y0,z0,v_z0)
sol=odeint(func,s0,t)

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
plt.show()

ani.save('hdfjh.gif')