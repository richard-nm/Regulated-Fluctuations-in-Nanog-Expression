from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


# basic model
def model(y,t,p):
    dydt=np.empty(2)
    N,a=y
    dydt[0]=an+(bn*N**n)/(kn**n+N**n)-d/cx*(bx*a**p)/(kx**p+a**p)*N-cn*N
    dydt[1]=aa+ba*a*N-ca*a
    return dydt

def hill():
    init=[0,0]
    p=[]
    m=[]
    sq=np.empty(150)
    t=np.logspace(0,7,num=100)
    for i in range(150):
        num=i*0.01+0.15
        p.append(num)
        md=odeint(model,init,t,args=(num,),mxstep=500000)
        dif = np.diff(md[95:, 0], n=0)
        var = np.var(dif)
        if var >1:
            sq[i] = 1
            m.append(num)
        else:
            sq[i] = 0
    plt.figure()
    plt.xlabel('Hill number p')
    plt.ylabel('Oscillation')
    plt.plot(p,sq)
    plt.plot(0.95,1,'ro')
    plt.plot(1.01, 1, 'ro')
    plt.show()
    print(m)




aa=0.005
an=0.1
ba=8e-9
bn=2.44
bx=50
kn=3750
kx=15000
ca=3e-5
cn=2.4e-4
cx=0.01
d=2e-7
n=2

hill()