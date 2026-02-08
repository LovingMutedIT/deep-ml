import math

def sigmoid(z: float) -> float:
	result = round(1 / (1+pow(math.e, -1*z)), 4)
	return result