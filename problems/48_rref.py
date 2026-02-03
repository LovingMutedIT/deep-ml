import numpy as np

def rref(matrix):
	# make the matrix only float point
	matrix = matrix.astype(float)

	row_len, col_len = matrix.shape
	locked_rows = []  #step 2

	for col_i in range(col_len):
		
		# selecting the pivot row
		pivot_row_i = -1

		for row_i in range(row_len):
			
			
			if row_i in locked_rows:
				continue
			
			if matrix[row_i][col_i] != 0:
				pivot_row_i = row_i
				break

		if pivot_row_i == -1:
			continue

		# bringing the pivot row to the next locked_row index
		next_pivot_row_i = (locked_rows[-1] + 1) if len(locked_rows) > 0 else 0

		if pivot_row_i != next_pivot_row_i:
			matrix[[next_pivot_row_i, pivot_row_i]] = matrix[[pivot_row_i, next_pivot_row_i]]

			pivot_row_i = next_pivot_row_i

		# scaling the pivot row with out pivot value
		pivot_value = matrix[pivot_row_i][col_i]
		matrix[pivot_row_i] = matrix[pivot_row_i]/pivot_value

		# eliminate all the numbers above and below
		for row_i in range(row_len):

			if row_i == pivot_row_i:
				continue

			# eliminate the column element by rescaling the whole row
			lead_coefficient = matrix[row_i][col_i]
			matrix[row_i] = matrix[row_i] - matrix[pivot_row_i] * lead_coefficient

		locked_rows.append(pivot_row_i)
	return matrix