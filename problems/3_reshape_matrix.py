import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

	# Write your code here and return a python list after reshaping by using numpy's tolist() method

	original_cols = len(a[0])
	original_rows = len(a)

	if (original_cols * original_rows) != (new_shape[0] * new_shape[1]):
		return []

	reshaped_matrix = []

	a_np_array = np.array(a)

	a_list = a_np_array.flatten().tolist()
	k = 0

	for i in range(new_shape[0]):
		reshaped_matrix.append([])
		for j in range(new_shape[1]):
			reshaped_matrix[i].append(a_list[k])
			k += 1

	return reshaped_matrix
