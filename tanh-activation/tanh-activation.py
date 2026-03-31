import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    y = np.where(x >= 0, 1 / (1 + np.exp(-2 *x)), np.exp( 2 * x) / (1 + np.exp(2 *x)))
    return 2 * y - 1
    pass