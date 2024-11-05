import math
import numpy as np


def single_neuron_model1(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    z = np.dot(features, weights) + bias
    probabilities = 1/(1+np.exp(-z))
    mse = sum((probabilities-labels)**2)/len(features)
    return np.round(probabilities,4), round(mse,4)



def single_neuron_model2(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
    mse = 0
    for feature_vector, label in zip(features, labels):
        z = sum(feature*weight for feature, weight in zip(feature_vector, weights)) + bias
        probability = round(1/(1+math.exp(-z)), 4)
        probabilities.append(probability)
        mse+= (probability-label)**2
    mse/=len(features)
    return probabilities, round(mse, 4)    
    
    
# Numpy Solution
print(single_neuron_model1([[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], [0, 1, 0], [0.7, -0.4], -0.1))


# Pythonic Solution
print(single_neuron_model2([[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], [0, 1, 0], [0.7, -0.4], -0.1))
