# A mix of Evensen'2009 and sakov'2008

from common import *

from mods.LA.fundamentals import sinusoidal_sample, Fmat, homogeneous_1D_cov

m = 1000
p = 4
obsInds = equi_spaced_integers(m,p)

tseq = Chronology(dt=1,dkObs=5,T=300,BurnIn=-1)

#def step(x,t,dt):
  #return np.roll(x,1,axis=x.ndim-1)
Fm = Fmat(m,-1,1,tseq.dt)
def step(x,t,dt):
  assert dt == tseq.dt
  return x @ Fm.T

f = {
    'm': m,
    'model': step,
    'noise': 0
    }

# In the animation, it can sometimes/somewhat occur
# that the truth is outside 3*sigma !!!
# Yet this is not so implausible because sinusoidal_sample()
# yields (multivariate) uniform (random numbers) -- not Gaussian.
wnum  = 25
X0 = RV(sampling_func = lambda N: \
    sqrt(5)/10 * sinusoidal_sample(m,wnum,N))

# TODO: Don't think this is quite right
#X0 = GaussRV(C=homogeneous_1D_cov(m,m/1,kind='Gauss'))


@atmost_2d
def hmod(E,t):
  return E[:,obsInds]

h = {
    'm': p,
    'model': hmod,
    'noise': GaussRV(C=0.01*eye(p))
    }
 
other = {'name': os.path.relpath(__file__,'mods/')}

params = OSSE(f,h,tseq,X0,**other)



####################
# Suggested tuning
####################