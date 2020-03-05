import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

N=200
t=np.linspace(0,31,N)

def func(s,t):
    f,v_f=s
    dfdt=v_f
    dv_fdt=(R*W**2*l*np.sin(W*t-f)-g*l*m*np.sin(f))/l**2*m
    
    return dfdt,dv_fdt

f0=np.pi/180*50
v_f0=0
m=100
g=9.81
R=15
l=15
W=0.2
s0=f0,v_f0

sol=odeint(func,s0,t)

x1=R*np.sin(W*t[:])
y1=-R*np.cos(W*t[:])

x2=x1+l*np.sin(sol[:,0])
y2=y1-l*np.cos(sol[:,0])

fig=plt.figure()
bodys=[]

for i in range(1,len(t),1):
    thisx=[0,x1[i],x2[i]]
    thisy=[0,y1[i],y2[i]]
    
    body_line,=plt.plot(thisx,thisy,'-o',color='r')
    bodys.append([body_line])

ani=ArtistAnimation(fig,bodys,interval=50)

plt.axis('equal')
plt.grid()

ani.save('HJHFFRY$G.gif')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    