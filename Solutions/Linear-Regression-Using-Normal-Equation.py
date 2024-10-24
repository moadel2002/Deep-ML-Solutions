import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    transpose = np.transpose(X)
    inv = np.linalg.inv(transpose @ X)
    theta = np.round(inv @ transpose @ y, 2).tolist()
    return theta


print(linear_regression_normal_equation([[1, 1], [1, 2], [1, 3]], [1, 2, 3]))