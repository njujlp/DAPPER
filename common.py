import numpy as np
import scipy as sp
import numpy.random
import scipy.linalg as sla
import numpy.linalg as nla
import scipy.stats as ss
import sys
import os.path
import importlib

import matplotlib
#matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')
plt.ion()
from mpl_toolkits.mplot3d import Axes3D

from numpy import sqrt, abs, floor, ceil, prod, \
    mean, \
    linspace, arange, reshape, \
    pi, log, \
    array, asarray, matrix, asmatrix, \
    eye, zeros, ones, diag, \
    trace, \
    dot

from scipy.linalg import sqrtm, inv, eigh, svd

np.set_printoptions(precision=5)
np.set_printoptions(suppress=True)
# Only applies to arrays. I.e. we will still
# get full precision by inspecting individual elements

from time import sleep


######################
# From DAPPER
######################

cwhite = array([1,1,1])
cred   = array([1,0,0])
cgreen = array([0,1,0])
cblue  = array([0,0,1])

from stoch import *
from utils import *
from misc import *
from viz import *
from chronos import *
from matrices import *
from randvars import *
from admin import *
from enkf_and_ienkf import *
