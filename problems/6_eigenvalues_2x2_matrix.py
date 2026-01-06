import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

    determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    trace = matrix[0][0] + matrix[1][1]

    eigen1 = ((trace) + math.sqrt((trace * trace) - (4*determinant))) / 2
    eigen2 = ((trace) - math.sqrt((trace * trace) - (4*determinant))) / 2

    eigenvalues = list()
    if eigen1 > eigen2:
        eigenvalues.append(eigen1)
        eigenvalues.append(eigen2)
    else:
        eigenvalues.append(eigen2)
        eigenvalues.append(eigen1)

    return eigenvalues
