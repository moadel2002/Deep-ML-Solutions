import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    scores = np.array(scores)
    maximum = np.max(scores)
    scaled = scores-maximum
    log_probs =scaled- np.log(np.sum(np.exp(scaled)))
    return np.round(log_probs, 4)


print(log_softmax([1,2,3]))