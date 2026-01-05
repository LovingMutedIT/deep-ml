def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    mat_rows = len(matrix)
    mat_cols = len(matrix[0])
    means = []
    if (mode == "row"):
        for i in range(mat_rows):
            means.append([])
            sum = 0
            for j in range(mat_cols):
                sum += matrix[i][j]
                if(j == mat_cols - 1):
                    mean = sum / (mat_cols)
                    means[i].append(mean)
    
    elif (mode == "column"):
        for i in range(mat_cols):
            sum = 0
            for j in range(mat_rows):
                sum += matrix[j][i]
                if(j == mat_rows - 1):
                    mean = sum / (mat_rows)
                    means.append(mean)

	return means
