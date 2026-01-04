def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	cols_a = len(a[0])
	rows_b = len(b)

	if cols_a != rows_b:
		return -1
	
	result = list()
	for i in range(len(a)):
		result.append(0)
	
	for i in range(len(a)):
		for k in range(len(a[0])):
			result[i] += a[i][k] * b[k]

	return result
