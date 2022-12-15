import numpy as np

def Problem4_2(A):
    return [A[i][j] for i in range(len(A)) for j in range(len(A[i])) if i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1]