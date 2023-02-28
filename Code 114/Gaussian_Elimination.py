import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    Ab = np.hstack((A, b.reshape(-1, 1)))  # augment the matrix A with column vector b
    for i in range(n):
        # Find the row with the largest absolute value in the i-th column
        max_row = i
        for j in range(i+1, n):
            if abs(Ab[j,i]) > abs(Ab[max_row,i]):
                max_row = j
        # Swap the i-th and max_row-th rows
        Ab[[i,max_row],:] = Ab[[max_row,i],:]
        # Reduce the i-th column to zeros below the i-th row
        for j in range(i+1, n):
            c = Ab[j,i] / Ab[i,i]
            Ab[j,:] -= c * Ab[i,:]
    # Solve for the unknowns using back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i,-1] - np.dot(Ab[i,:-1], x)) / Ab[i,i]
    return x
# Example system of linear equations:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3
# x= 2, y= 3, z= -1
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

b = np.array([8, -11, -3])
A = A.astype(np.float64)
b = b.astype(np.float64)
x = gaussian_elimination(A, b)
print(x)