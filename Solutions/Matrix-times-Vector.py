from typing import Union
import numpy as np

def matrix_dot_vector1(a: list[list[Union[int, float]]], b: list[Union[int, float]]) -> list[Union[int, float]]:
	return -1 if len(a[0]) != len(b) else np.dot(a, b).tolist()


def matrix_dot_vector2(a: list[list[Union[int, float]]], b: list[Union[int, float]]) -> list[Union[int, float]]:
    if len(a[0])!=len(b):
        return -1

    dot_vector = []
    for row in a:
        dot_vector.append(sum(row[col]*b[col] for col in range(len(row))))   
    return dot_vector         
    


a = [[1,2],[2,4]]
b = [1,2]

# Using numpy builtin function
print(matrix_dot_vector1(a,b))

# Manual matrix-vector multiplication using basic Python operations
print(matrix_dot_vector2(a,b))