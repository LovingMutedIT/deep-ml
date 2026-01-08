def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    if(det == 0):
        return None
    
    inverted_matrix = []
    k = len(matrix) - 1
    for i in range(len(matrix[0])):
        inverted_matrix.append([])
        for j in range(len(matrix)):
            if(i == j):
                inverted_matrix[i].append(matrix[k][k] / det)
                k -= 1
                continue
            inverted_matrix[i].append(matrix[i][j] / det * -1)

    return inverted_matrix
