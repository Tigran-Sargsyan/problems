import numpy as np

def det(A):
    """A function to compute the determinant of a square matrix"""
    assert isinstance(A,np.ndarray) and (A.shape[0]==A.shape[1])
    res = 0
    if len(A) == 2:
        # Base case: Computing the determinant of 2x2 size matrix
        res = A[0,0]*A[1,1] - A[0,1]*A[1,0]
        return res
    else:
        # Calculation via the the first column
        for k in range(len(A)):
            B = np.vstack((A[0:k,1:],A[k+1:,1:]))
            res += (-1) ** k * A[k,0] * det(B)
        return res

# Testing 
for i in range(10):
    ary = np.random.randint(10,size=(4,4))
    print("My function: ",det(ary))
    print("linalg module", np.linalg.det(ary))