#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    pow_matrix = []
    for row in matrix:
        squared_integers = list(map(lambda num: num ** 2, row))
        pow_matrix.append(squared_integers)
    return pow_matrix
