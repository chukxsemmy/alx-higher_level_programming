#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sqr_val = matrix.copy()
    for i in range(len(matrix)):
        sqr_val[i] = list(map(lambda x: x**2, matrix[i]))
    return (sqr_val)
