from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
from Regulated_Nanog import simulation,get_arrow,nullN,nulla,steady


# parameters for simulation
x=y=np.logspace(2,4,num=100)
s1=fsolve(steady,1500)
t = np.logspace(0, 7, num=400)
# draw plot
plt.figure()
get_arrow()
simulation(5)
# streamplot()
plt.plot(x,nullN(x),label='Nanog')
plt.plot(nulla(y),y,label='Oct4')
plt.xlim([100,10000])
plt.ylim([100,10000])
plt.plot(s1,nullN(np.array(s1)),'ro')
plt.xlabel('Nanog (# of molecules)')
plt.ylabel('Oct4 (# of molecules)')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.show()
