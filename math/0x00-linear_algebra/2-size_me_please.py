#!/usr/bin/env python3
"""aaaaaaaaaaaaaa """
def matrix_shape(matrix):
    """ ssssssss """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    """ fffffff"""
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
