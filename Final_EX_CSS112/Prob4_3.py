import numpy as np

def Problem4_3(A): 
    det = np.linalg.det(A)
    a, b, c, d = A.flatten()
    A_inv = 1/det * np.array([[d, -b], [-c, a]])
    return A_inv