from sympy import *
L=Function('L')
f1=Function('f1')
f2=Function('f2')
vf1=Function('vf1')
vf2=Function('vf2')



t=Symbol('t')
m1=Symbol('m1')
m2=Symbol('m2')
l1=Symbol('l1')
l2=Symbol('l2')
g=Symbol('g')

L=(m1+m2)*l1**2*vf1(t)**2/2+m2*l2**2*vf2(t)**2 \
    +m2*l1**vf1(t)*vf2(t)*l2*cos(f1(t)-f2(t))+(m1+m2)*g*l1*cos(f1(t))+m2*g*l2*cos(f2(t))

print(diff(L,f2(t)))
