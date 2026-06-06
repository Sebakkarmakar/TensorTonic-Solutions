import numpy as np

def matrix_trace(A):
    row=len(A)
    col=len(A[0])
    total=0
    for i in range(row):
        for j in range(col):
            if i==j:
                total+=A[i][j]
    return total