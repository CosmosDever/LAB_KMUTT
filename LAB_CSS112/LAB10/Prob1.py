import numpy as np


def Problem1(n): 
    onesk = np.ones((n,n))
    indx = [(i,j+1) for j in range(n-1) for i in range(j+1)]
    xyindx = tuple(zip(*indx))
    onesk[xyindx] = 0
    return onesk