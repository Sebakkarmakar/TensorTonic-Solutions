import numpy as np

def relu(x):
    arr=np.array(x)
    output=np.maximum(0,arr)
    return output