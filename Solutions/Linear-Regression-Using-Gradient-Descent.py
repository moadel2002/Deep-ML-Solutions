from math import cos
import numpy as np
def linear_regression_gradient_descent1(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    # Your code here, make sure to round
    m, n = X.shape
    theta = np.zeros((n, 1))
    y = y.reshape(-1,1)
    for i in range(iterations):
        cost = 0
        for j in range(m): 
            xi = X[j].reshape(1,-1)
            cost+= ((xi @ theta - y[j]) @ xi)
        cost/=m
        theta = theta - alpha*cost.T
        
    return np.round(theta,4).flatten()


def linear_regression_gradient_descent2(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    y = y.reshape(-1,1)
    for i in range(iterations):
        cost = (X.T @ (X @ theta - y))/m
        theta = theta - alpha*cost
        
    return np.round(theta, 4).flatten()


X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000

# Solution without Victorization
print(linear_regression_gradient_descent1(X, y, alpha, iterations))


# Solution with Victorization
print(linear_regression_gradient_descent2(X, y, alpha, iterations))


