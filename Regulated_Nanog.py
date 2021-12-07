from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

import random

# basic model
def model(y,t):
    dydt=np.empty(2)
    N,a=y
    dydt[0]=an+(bn*N**n)/(kn**n+N**n)-d/cx*(bx*a**p)/(kx**p+a**p)*N-cn*N
    dydt[1]=aa+ba*a*N-ca*a
    return dydt

# model for streamplot drawing with array output
def smodel(y,t):
    N,a=y
    dndt=an+(bn*N**n)/(kn**n+N**n)-d/cx*(bx*a**p)/(kx**p+a**p)*N-cn*N
    dadt=aa+ba*a*N-ca*a
    return np.array([dndt,dadt])

# find the intersection point
def steady(N):
    return nulla(nullN(N))-N

# nullcline for dN/dt
def nullN(N):
    ep = bx * d / cx
    A = (an + (bn * N ** n) / (kn ** n + N ** n) - cn * N) / (N * ep)
    raw=A/(1-A)*kx**p
    return np.power(np.abs(raw),1/p)*np.sign(raw)

# nullcline for dA/dt
def nulla(a):
    return (ca * a-aa)/(ba * a)

# do random initial states simulation
def simulation(number):
    '''
    :param number: times you want to simulate
    :return: make plots
    '''
    for i in range(number):
        a=random.randint(0,2000)
        b=random.randint(0,2000)
        init=[a,b]
        y=odeint(model,init,t,mxstep=500000)
        plt.plot(a,b,'bo')
        plt.plot(y[:,0],y[:,1],alpha=0.2,color='green')
        plt.plot(y[-1:,0],y[-1:,1],'bs')

# draw streamplot
def streamplot():
    nx=ay=np.linspace(100,10000,12)
    X,Y=np.meshgrid(nx,ay)
    dX,dY=smodel([X,Y],0.0)
    norm=np.sqrt(dX**2+dY**2)
    plt.streamplot(X,Y,dX,dY,color=norm,cmap=plt.cm.cool,density=3)

# draw arraw indicators
def get_arrow():
    for i in range(20):
        if i<=9:
            i=10**(i/10+2)
        else:
            i=10**(i%10/10+3)
        for k in range(20):
            if k<=9:
                k=10**(k/10+2)
            else:
                k=10**(k%10/10+3)
            init=[i,k]
            md=odeint(model,init,t,mxstep=500000)
            plt.arrow(i,k,md[40][0]-i,md[40][1]-k,width=0.002)


# parameters for equations   a-> alpha, b-> beta, c-> gama, d-> lambda
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
p=1.5

# parameters for simulation
x=y=np.logspace(2,4,num=100)
t = np.logspace(0, 7, num=100)

