import numpy as np
# Problem 4.1 Broadcasting
def Problem4_1(A,B):
    return A + B[:, np.newaxis]