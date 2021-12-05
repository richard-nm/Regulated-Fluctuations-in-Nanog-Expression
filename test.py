import numpy as np
import matplotlib.pyplot as plt
import stochpy

smod=stochpy.SSA()
smod.Model('nanog expression.psc',dir='C:/Users/PC/PycharmProjects/untitled/PSB/Final Assignment/')
smod.ChangeParameter('omega',1)
smod.DoStochSim(end=900000, mode= 'time', trajectories= 1, quiet= False)
smod.PlotSpeciesTimeSeries(species2plot=['proteinN'])
stochpy.plt.xlabel('Time (hours)')
stochpy.plt.ylabel('Nanog (molec)')
stochpy.plt.xticks(np.array([i for i in range(0,990000,90000)]),[str(i*250) for i in range(11)])
stochpy.plt.yscale('log')
plt.show()
