from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from Regulated_Nanog import model



# draw integrate plot
t = np.logspace(0, 6, num=100)
plt.figure()
ry=odeint(model,[1000,1000],t,mxstep=500000)
plt.plot(t,ry[:,0],label='N')
plt.plot(t,ry[:,1],label='A')
plt.xlabel('Nanog (# of molecules)')
plt.ylabel('Oct4 (# of molecules)')
plt.legend()
plt.show()
