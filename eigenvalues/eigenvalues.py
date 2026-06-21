import numpy as np

def calculate_eigenvalues(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0:
        return None
    if not isinstance(matrix[0], list):
        return None
    row=len(matrix)
    col=len(matrix[0])
    if row==col:
        output,_=np.linalg.eig(matrix)
        return output
    elif row and col is None:
        return None
    else:
        return None