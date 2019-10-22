print('-----------задание 1--------------')
from pitconst import g
from math import tan, cos, pi
h=100
B=30
a=pi/3 
u=((g*h*(tan(B)**2))/(2*(cos(a)**2)*(1-tan(B)*tan(a))))**0.5
print(u)
print('-----------задание2-------------')
from pitconst import k, h, El
T=200
E=300
N=(2/(pi)**0.5)*(h/(k*T)**1.5)*(El**-E/(k*T))*(E**(T/2))
print(N)
 

