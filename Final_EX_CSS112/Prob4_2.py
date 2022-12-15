import numpy as np
#Problem 4.2 
def Problem4_2(A):
    return np.array(A[np.arange(0, A.shape[0], 2), np.arange(0, A.shape[0], 2) % 2]) 