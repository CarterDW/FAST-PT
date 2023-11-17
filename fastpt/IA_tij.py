from __future__ import division
import numpy as np
from .J_table import J_table 
import sys
from time import time
from numpy import log, sqrt, exp, pi
from scipy.signal import fftconvolve as convolve

def IA_tij_feG2():
    # Ordering is \alpha, \beta, l_1, l_2, l, A coeficient
    l_mat_tij_feG2=np.array([[0,0,0,2,0,13/21],\
            [0,0,0,2,2,8/21],\
            [1,-1,0,2,1,1/2],\
            [-1,1,0,2,1,1/2]], dtype=float)
    table=np.zeros(10,dtype=float)
    for i in range(l_mat_tij_feG2.shape[0]):
        x=J_table(l_mat_tij_feG2[i])
        table=np.row_stack((table,x))
    return table[1:,:]

def IA_tij_heG2():
    # Ordering is \alpha, \beta, l_1, l_2, l, A coeficient
    l_mat_tij_heG2=np.array([[0,0,0,0,0,-9/70],\
            [0,0,2,0,0,-26/63],\
            [0,0,0,0,2,-15/49],\
            [0,0,2,0,2,-16/63],\
            [0,0,1,1,1,81/70],\
            [0,0,1,1,3,12/35],\
            [0,0,0,0,4,-16/245],\
            [1,-1,0,0,1,-3/10],\
            [1,-1,2,0,1,-1/3],\
            [1,-1,1,1,0,1/2],\
            [1,-1,1,1,2,1],\
            [1,-1,0,2,1,-1/3],\
            [1,-1,0,0,3,-1/5]], dtype=float)
    table=np.zeros(10,dtype=float)
    for i in range(l_mat_tij_heG2.shape[0]):
        x=J_table(l_mat_tij_heG2[i])
        table=np.row_stack((table,x))
    return table[1:,:]
