import numpy as np

def accuracy_score1(y_true, y_pred):
    f = sum(true==pred for true, pred in zip(y_true, y_pred))
    accuracy = f/len(y_true)
    return accuracy


def accuracy_score(y_true, y_pred):
    accuracy = np.mean(y_true==y_pred)
    return accuracy


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])

# Pythonic Solution
output = accuracy_score1(y_true, y_pred)
print(output)

# Numpy Solution
output = accuracy_score(y_true, y_pred)
print(output)