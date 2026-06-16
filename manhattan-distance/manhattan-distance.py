import numpy as np

def manhattan_distance(x, y):
    x=np.array(x)
    y=np.array(y)
    distance=np.sum(abs(x-y))
    return int(distance)
    