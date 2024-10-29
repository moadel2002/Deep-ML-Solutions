import numpy as np

def transpose_matrix1(a: list[list[int|float]]) -> list[list[int|float]]:
    transpose = np.zeros((len(a[0]), len(a)))
    for i in range(len(a)):
        for j in range(len(a[i])):
            transpose[j][i] = a[i][j]
    
    return transpose.tolist()


def transpose_matrix2(a: list[list[int|float]]) -> list[list[int|float]]:
    return [list(i) for i in zip(*a)]


a = [[1,2,3],[4,5,6]]

# numpy solution
print(transpose_matrix1(a))

# pythonic solution
print(transpose_matrix2(a))


