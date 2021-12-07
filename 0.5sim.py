import matplotlib.pyplot as plt
import stochpy
import numpy as np

smod=stochpy.SSA()
smod.Model('0.5sim.psc',dir='C:/Users/PC/PycharmProjects/untitled/PSB/Final Assignment/')
smod.ChangeParameter('omega',1)
ts=90000
ns=10000
# ta=np.linspace(0,ts,ns)
smod.DoStochSim(end=ts, mode= 'time', trajectories= 1, quiet= False)
smod.PlotSpeciesTimeSeries(species2plot=['proteinN'])
stochpy.plt.xlabel('Time (hours)')
stochpy.plt.ylabel('Nanog (molec)')
stochpy.plt.xticks(np.array([i for i in range(0,99000,9000)]),[str(i*250) for i in range(11)])
plt.show()
# smod.PlotSpeciesDistributions(species2plot='proteinN')
smod.GetRegularGrid(n_samples=ns)
data=smod.data_stochsim_grid.species
plt.figure()
plt.hist(data[4],bins=1000)
stochpy.plt.ylabel('Counts')
stochpy.plt.xlabel('Nanog (molec)')
plt.xlim([10,10000])
plt.xscale('log')
# plt.figure()
plt.show()

