import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X = np.array(X)
    y = np.array(y)

    # solved using ridge regression here to avoid singular matrix inverse error in np.linalg
    lambda_val = 1e-5
    I = np.eye(X.shape[1])
    X_transpose = X.T
    XTX = X_transpose @ X

    XTX_inverse = np.linalg.inv(XTX + lambda_val * I)

    theta = XTX_inverse @ X_transpose @ y
    theta_rounded = np.rint(theta)

    return theta_rounded
