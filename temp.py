import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

t=np.arange(0,100,0.1)
def func(z,t):
    x,v_x,y,v_y=z
    dxdt=v_x
    dv_xdt=(F1+F2*np.cos(A)+F3*np.cos(2*A)+F4*np.cos(3*A))/m
    dydt=v_y
    dv_ydt=(F4+F3*np.cos(A)+F2*np.cos(2*A)+F1*np.cos(3*A))/m
    return dxdt,  dv_xdt, dydt,  dv_ydt

x0=0
v_x0=-10
y0=0
v_y0=-30
z0=x0, v_x0, y0, v_y0

F1=10
F2=20
F3=30
F4=40
m=65
A=0.524
sol=odeint(func,z0,t)

fig=plt.figure()
sili=[]

for i in range(0,len(t),1):
    Fas,=plt.plot(sol[:i,0],sol[:i,2],'-',color='r')
    Fas_line,=plt.plot(sol[i,0],sol[i,2],'o',color='r')
    sili.append([Fas,Fas_line])
ani=ArtistAnimation(fig,sili,interval=50)
plt.axis('equal')
ani.save('sili.gif')    



 

    


    