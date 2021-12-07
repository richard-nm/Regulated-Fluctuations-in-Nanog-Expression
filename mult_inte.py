from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from Hill_number import model


# draw integrate plot
t = np.logspace(0, 6, num=100)
plt.figure()
plt.subplot(3,1,1)
ry=odeint(model,[1000,1000],t,mxstep=500000,args=(1.5,))
plt.plot(t,ry[:,0],label='N')
plt.plot(t,ry[:,1],label='A')


plt.legend()
plt.subplot(3,1,2)
ry=odeint(model,[1000,1000],t,mxstep=500000,args=(1,))
plt.plot(t,ry[:,0],label='N')
plt.plot(t,ry[:,1],label='A')

plt.ylabel('Oct4 (# of molecules)')
plt.legend()
plt.subplot(3,1,3)
ry=odeint(model,[1000,1000],t,mxstep=500000,args=(0.5,))
plt.plot(t,ry[:,0],label='N')
plt.plot(t,ry[:,1],label='A')
plt.xlabel('Nanog (# of molecules)')

plt.legend()
plt.show()