def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    trans_a = []
    for i in range(len(a[0])):
        trans_a.append([])
        for j in range(len(a)):
            trans_a[i].append(a[j][i])

    return trans_a
    
