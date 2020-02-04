import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
t=np.arange(10**(-7), 1.3*10**(-7), 10**(-9))


A=0.008
k=9*10**9
q1=-1.1*10**(-13)
q2=1.1*10**(-13)
q3=-1.1*10**(-13)
q4=1.1*10**(-13)

M1=1.1*10**(-27)
M2=1.1*10**(-27)
M3=1.1*10**(-27)
M4=1.1*10**(-27)

V=1.5*10**6

def func(s,t):
    (x1,v_x1,y1,v_y1,
     x2,v_x2,y2,v_y2,
     x3,v_x3,y3,v_y3,
     x4,v_x4,y4,v_y4)=s
    dxdt1=v_x1
    dv_xdt1=(k*q2*q1/M1*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5)+(k*q3*q1/M1*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5)+(k*q4*q1/M1*(x1-x4)/((x1-x4)**2+(y1-y4)**2)**1.5)
    
    dydt1=v_y1
    dv_ydt1=(k*q2*q1/M1*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5)+(k*q3*q1/M1*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5)+(k*q4*q1/M1*(y1-y4)/((x1-x4)**2+(y1-y4)**2)**1.5)
    
    dxdt2=v_x2
    dv_xdt2=(k*q2*q1/M2*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5)+(k*q3*q2/M2*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5)+(k*q4*q2/M2*(x2-x4)/((x2-x4)**2+(y2-y4)**2)**1.5)
    
    dydt2=v_y2
    dv_ydt2=(k*q2*q1/M2*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5)+(k*q3*q2/M2*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5)+(k*q4*q2/M2*(y2-x4)/((x2-x4)**2+(y2-y4)**2)**1.5)
    
    dxdt3=v_x3
    dv_xdt3=(k*q2*q1/M3*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5)+(k*q3*q2/M3*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5)+(k*q4*q3/M3*(x3-x4)/((x3-x4)**2+(y3-y4)**2)**1.5)
    
    dydt3=v_y3
    dv_ydt3=(k*q3*q2/M3*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5)+(k*q3*q2/M3*(y3-y2)/((x3-x2)**2+(y3-y2)**2)**1.5)+(k*q4*q3/M3*(y3-x4)/((x3-x4)**2+(y3-y4)**2)**1.5)
    
    dxdt4=v_x4
    dv_xdt4=(k*q1*q4/M3*(x4-x1)/((x4-x1)**2+(y4-y1)**2)**1.5)+(k*q2*q4/M3*(x4-x2)/((x4-x2)**2+(y4-y2)**2)**1.5)+(k*q4*q3/M4*(x4-x3)/((x4-x3)**2+(y4-y3)**2)**1.5)
    
    dydt4=v_y4
    dv_ydt4=(k*q1*q4/M4*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5)+(k*q2*q4/M3*(y4-y2)/((x4-x2)**2+(y4-y2)**2)**1.5)+(k*q4*q3/M4*(y4-y3)/((x4-x3)**2+(y4-y3)**2)**1.5)
    
    
    
    
    
    return ( dxdt1,dv_xdt1,dydt1,dv_ydt1,
            dxdt2,dv_xdt2,dydt2,dv_ydt2,
            dxdt3,dv_xdt3,dydt3,dv_ydt3,
            dxdt4,dv_xdt4,dydt4,dv_ydt4)
x10=A
v_x10=A-V*2**0.5/2
y10=A
v_y10=A+V*2**0.5/2

x20=A
v_x20=A+V*2**0.5/2
y20=-A
v_y20=-A+V*2**0.5/2

x30=-A 
v_x30=-A+V*2**0.5/2
y30=-A
v_y30=-A-V*2**0.5/2

x40=-A
v_x40=-A-V*2**0.5/2
y40=A

v_y40=A-V*2**0.5/2
s0=(x10,v_x10,y10,v_y10,
    x20,v_x20,y20,v_y20,
    x30,v_x30,y30,v_y30,
    x40,v_x40,y40,v_y40)



sol=odeint(func,s0,t)
fig=plt.figure()
bodys=[]
for i in range(0,len(t),1):
    
    body1,=plt.plot(sol[:i,0],sol[:i,2],'-',color='r')
    body1_line,=plt.plot(sol[i,0],sol[i,2],'o',color='r')
    
    body2,=plt.plot(sol[:i,4],sol[:i,6],'-',color='g')
    body2_line,=plt.plot(sol[i,4],sol[i,6],'o',color='g')
    
    body3,=plt.plot(sol[:i,8],sol[:i,10],'-',color='b')
    body3_line,=plt.plot(sol[i,8],sol[i,10],'o',color='b')
    
    body4,=plt.plot(sol[:i,12],sol[:i,14],'-',color='k')
    body4_line,=plt.plot(sol[i,12],sol[i,14],'o',color='k')
    
    bodys.append([body1,body1_line,body2,body2_line,body3,body3_line,body4,body4_line])
    
ani=ArtistAnimation(fig,bodys,interval=50)
plt.axis('equal')
ani.save('N_body_K.gif')    

