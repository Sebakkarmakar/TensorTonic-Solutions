import numpy as np

def leaky_relu(x, alpha=0.01):
    arr=np.array(x)
    res=[alpha*x if x<0 else x for x in arr]
    return np.array(res)
   