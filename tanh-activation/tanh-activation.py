import numpy as np

def tanh(x):
    res=[]
    arr=np.array(x)
    for i in arr:
        up=np.exp(i)-np.exp(-i)
        down=np.exp(i)+np.exp(-i)
        res.append(up/down)
    return np.array(res)