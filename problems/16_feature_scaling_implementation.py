import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
    col_means = np.mean(data, axis=0)
    col_stds = np.std(data, axis=0)

    standardized_data = np.round(((data - col_means) / col_stds), decimals=4)

    col_min = np.min(data, axis=0)
    col_max = np.max(data, axis=0)

    normalized_data = np.round(((data - col_min) / (col_max - col_min)), decimals=4)

    return standardized_data, normalized_data
