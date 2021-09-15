#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    modified_matrix = [[i ** 2 for i in mat] for mat in matrix]
    return modified_matrix
