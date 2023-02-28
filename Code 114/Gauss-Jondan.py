import numpy as np

def gauss_jordan(A, b):
    # augment the matrix A with column vector b
    Ab = np.hstack((A, b.reshape(-1, 1)))

    # apply Gauss-Jordan elimination
    n = Ab.shape[0]
    for i in range(n):
        # find the row with the largest pivot
        max_row = i
        for j in range(i+1, n):
            if abs(Ab[j,i]) > abs(Ab[max_row,i]):
                max_row = j
        
        # swap the rows to make the pivot the largest
        Ab[[i,max_row],:] = Ab[[max_row,i],:]
        
        # divide the pivot row by the pivot
        pivot = Ab[i,i]
        Ab[i,:] /= pivot
        
        # subtract multiples of the pivot row from the other rows
        for j in range(n):
            if j != i:
                c = Ab[j,i]
                Ab[j,:] -= c * Ab[i,:]
    
    # extract the solution vector from the augmented matrix
    x = Ab[:,n]
    
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
x = gauss_jordan(A, b)
print(x)