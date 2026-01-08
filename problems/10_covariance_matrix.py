def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
    cov_mat = []

    for i in range(len(vectors)):
        cov_mat.append([])
        for j in range(len(vectors)):
            sum1 = 0
            sum2 = 0
            for k in range(len(vectors[0])):
                sum1 += vectors[i][k]
                sum2 += vectors[j][k]
            mean1 = sum1 / len(vectors[0])
            mean2 = sum2 / len(vectors[0])
            cov = 0.0
            for k in range(len(vectors[0])):
                cov += (vectors[i][k] - mean1) * (vectors[j][k] - mean2)
            cov_mat[i].append(cov / (len(vectors[0]) - 1))
    return cov_mat
