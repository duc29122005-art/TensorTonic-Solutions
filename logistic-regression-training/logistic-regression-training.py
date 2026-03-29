import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    m, n = X.shape
    
    # Khởi tạo
    w = np.zeros(n)
    b = 0.0

    for _ in range(steps):
        # Forward
        z = np.dot(X, w) + b
        P = _sigmoid(z)

        # Gradient
        dz = P - y
        dw = (1/m) * np.dot(X.T, dz)
        db = (1/m) * np.sum(dz)

        # Update
        w -= lr * dw
        b -= lr * db

    return w, b
    
    # Write code here
    pass