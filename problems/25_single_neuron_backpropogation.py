import math
import numpy as np

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	mse_values = []
	for i in range(epochs):
		mse_loss, sigmoid_values, sigmoid_gradients = loss_sigmoid_gradient_calculation(features, labels, initial_weights, initial_bias)
		mse_values.append(mse_loss)

		for j in range(len(initial_weights)):
			sum_weights = 0
			for k in range(len(features)):
				sum_weights += (sigmoid_values[k] - labels[k]) * sigmoid_gradients[k] * features[k][j]

			mse_weight_gradient = round(2 * sum_weights / len(features), 4)

			initial_weights[j] = round(initial_weights[j] - (learning_rate * mse_weight_gradient), 4) 
		
		sum_bias = 0
		for l in range(len(features)):
			sum_bias += (sigmoid_values[l] - labels[l]) * sigmoid_gradients[l]
		
		mse_bias_gradient = round(2 * sum_bias / len(features),4)
		initial_bias = round(initial_bias - (learning_rate * mse_bias_gradient), 4)

	updated_weights = initial_weights
	updated_bias = initial_bias
	
	return updated_weights, updated_bias, mse_values

def loss_sigmoid_gradient_calculation(features: np.ndarray, labels: np.ndarray, weights: np.ndarray, bias: float):
	errors = 0
	sigmoid_values = []
	sigmoid_gradients = []
	for j in range(len(features)):
		w_sum = 0
		for k in range(len(features[0])):
			w_sum += features[j][k] * weights[k]
		w_sum += bias
		prob = round(1 / (1+pow(math.e, -1*w_sum)), 4)
		errors += round(pow(prob - labels[j], 2),4)
		sigmoid_values.append(prob)
		sigmoid_gradients.append(round(prob * (1 - prob),4))

	mse_loss = round(errors / len(features), 4)
	return mse_loss, sigmoid_values, sigmoid_gradients