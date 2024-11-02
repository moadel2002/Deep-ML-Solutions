import math
import numpy as np

def softmax1(scores: list[float]) -> list[float]:
    probabilities = np.exp(scores)/sum(np.exp(scores))
    return np.round(probabilities,4)


def softmax2(scores: list[float]) -> list[float]:
    exp_sum = sum([math.exp(score) for score in scores])
    probabilities = [round(math.exp(score)/exp_sum,4) for score in scores]
    return probabilities


# Numpy Solution
print(softmax1([1,2,3]))


# Pythonic Solution
print(softmax2([1,2,3]))
