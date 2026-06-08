import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    arr=np.array(x)
    output=[lam*i if i>0 else lam*alpha*(np.exp(i)-1) for i in arr]
    return output