import numpy as np
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:

	points = np.array(points)
	initial_centroids = np.array(initial_centroids)

	for i in range(max_iterations):
		distances = np.linalg.norm(points[:, None] - initial_centroids[None, :], axis = -1)

		min_indices = np.argmin(distances, axis=1)

		new_means = []
		for j in range(k):
			assigned_points = points[min_indices == j]
			if len(assigned_points) > 0:
				new_means.append(assigned_points.mean(axis=0))
			else:
				new_means.append(initial_centroids[i])
			
		cluster_means = np.array(new_means)
		initial_centroids = cluster_means
	
	final_centroids = [tuple(row) for row in cluster_means]


	return final_centroids