import numpy as np
import math

def gelu(x):
    arr=np.array(x)
    erf_vec = np.vectorize(math.erf)
    output=(0.5*arr*(1+erf_vec(arr/np.sqrt(2))))
    return np.array(output)