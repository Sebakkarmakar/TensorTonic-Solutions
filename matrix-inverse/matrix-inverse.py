import numpy as np

def matrix_inverse(A):
    arr=np.array(A)
    det_val=np.linalg.det(arr)
    if det_val==0:
        return None
    else:
        output=np.linalg.inv(arr)
        return output
    