import matplotlib.pyplot as plt
import stochpy
import numpy as np

smod=stochpy.SSA()
smod.Model('nanog_expression.psc',dir='C:/Users/PC/PycharmProjects/untitled/PSB/Final Assignment/')
smod.ChangeParameter('omega',0.2)
ts=900000
ns=10000

smod.DoStochSim(end=ts, mode= 'time', trajectories= 1, quiet= False)
smod.PlotSpeciesTimeSeries(species2plot=['proteinN'])
stochpy.plt.xlabel('Time (hours)')
stochpy.plt.ylabel('Nanog (molec)')
stochpy.plt.xticks(np.array([i for i in range(0,990000,90000)]),[str(i*250) for i in range(11)])
# stochpy.plt.yscale('log')
plt.show()

smod.GetRegularGrid(n_samples=ns)
data=smod.data_stochsim_grid.species
plt.figure()
plt.hist(data[4],bins=1000)
plt.xlabel('Nanog (molec)')
plt.ylabel('Count')
plt.xlim([10,10000])
plt.xscale('log')
plt.show()

