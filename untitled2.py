from untitled0 import Cv
m=1.4*10**14
def mu_mit(ma, V):
    T=(ma*V**2)/(2*Cv*m)
    if T>=50:
        print('SMERT')
    elif T>=30 and T<50:
        print('POCHTI SMERT')
    else:
        a=((Cv*m*100*2)/ma)**-0.5
        print(a)
        
        print('POVEZLO')
        

mu_mit(5768756635,67647653786)        