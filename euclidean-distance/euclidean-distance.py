import numpy as np

def euclidean_distance(x, y):
    x=np.array(x)
    y=np.array(y)
    total=(x-y)**2
    euclidean_distance=np.sqrt(sum(total))
    return float(euclidean_distance)