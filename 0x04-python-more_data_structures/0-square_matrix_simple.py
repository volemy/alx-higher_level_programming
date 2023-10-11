#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    output = []
    for i in range(len(matrix)):
        output.append(list(map(lambda x: x ** 2, matrix[i])))
    return output
