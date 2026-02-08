import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):

	probabilities = []
	mse = 0
	for i in range(len(features)):
		w_sum = 0
		for j in range(len(features[0])):
			w_sum += features[i][j] * weights[j]
		w_sum += bias
		prob = round(1 / (1 + pow(math.e, -1*w_sum)), 4)
		probabilities.append(prob)
		squared_err = round(pow(labels[i] - prob,2),4)
		mse += squared_err

	mse = round(mse / len(features), 4)
	return probabilities, mse