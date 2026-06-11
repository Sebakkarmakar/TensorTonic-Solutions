import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p=np.array(p)
    y=np.array(y)
    loss = -(y * ((1 - p) ** gamma) * np.log(p) +(1 - y) * (p ** gamma) * np.log(1 - p))
    return np.mean(loss)