import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	
    x = [0, 0, 0]
    x_new = [0, 0, 0]
    for k in range(n):
        for i in range(len(A[0])):
            sum = 0
            for j in range(len(A[0])):
                if (j == i):
                    continue
                sum += A[i][j] * x[j]
            sum = np.round(((b[i] - sum) / A[i][i]), decimals=4)
            x_new[i] = sum
        for i in range(len(A[0])):
            x[i] = x_new[i]
    return x
