# Stochastic Simulation Algorithm input file

# Reactions
R1:
	pn > pn + mRNAn
	k1*omega*pn
R2:
	pa > pa + mRNAa
	k2*omega*pa
R3:
	mRNAn > mRNAn + proteinN
	k3*mRNAn
R4:
	mRNAas > mRNAas + proteinAs
	k4*mRNAas
R5:
	mRNAa > mRNAa + proteinA
	k5*mRNAa
R6:	
	pa+proteinA +proteinN  >pa+proteinA +proteinN + mRNAa
	pa*proteinA*proteinN*k6/omega
R7:
	proteinN + proteinAs> proteinAs
	proteinN*proteinAs*k7/omega
R8:
	mRNAn >$pool
	k8*mRNAn
R9:
	mRNAas >$pool
	k9*mRNAas
R10:
	mRNAa >$pool
	k10*mRNAa
R11:
	proteinN>$pool
	k11*proteinN
R12:
	proteinA>$pool
	k12*proteinA
R13:
	proteinAs>$pool
	k13*proteinAs
R14:
    pn>pn+mRNAn
	pn*k14*omega*proteinN**2/((kn*omega)**2+proteinN**2)
R15:
	pa>pa+mRNAas
	pa*k15*omega*proteinA**1.5/((kx*omega)**1.5+proteinA**1.5)


# Fixed species

# Variable species

mRNAn=0
mRNAa=0
mRNAas=0
proteinAs=0
proteinA=3000
proteinN=3000

# Parameters

k1=0.1/40
k2=0.005/40
k3=0.2
k4=0.2
k5=0.2
k6=(8e-9)/40
k7=2e-7
k8=0.005
k9=0.005
k10=0.005
k11=2.4e-4
k12=3e-5
k13=0.01
k14=2.44/40
k15=50/40
omega=1
kx=15000
kn=3750
pa=1
pn=1
