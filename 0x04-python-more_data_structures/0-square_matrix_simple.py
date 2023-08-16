#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for index in range(len(matrix)):
        new_matrix[index] = list(map(lambda x: x**2, matrix[index]))

    return new_matrix
