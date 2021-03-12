#!/usr/bin/env python3



def matrix_shape(matrix):
    '''dddddddddddddddddddddddddd'''
    if type(matrix[0]) is not list:
        '''fffff'''
        return [len(matrix)]
    else:
        '''aaaaaaaaaaaaaaaaa'''
        return [len(matrix)] + matrix_shape(matrix[0])


def concat_recursive(mat1, mat2, axe):
    '''ddddddddddddddddddddaaaaaaaaaaaaaaaaaadddddd'''
    result = []
    if axe == 0:
        result = mat1 + mat2
        return result
    for i in range(len(mat1)):
        result.append(concat_recursive(mat1[i], mat2[i], axe - 1))
    return result


def cat_matrices(mat1, mat2, axis=0):
    '''ttttttttttttttttt'''
    if len(matrix_shape(mat1)) > axis and len(matrix_shape(mat2)) > axis:
        return concat_recursive(mat1, mat2, axis)
    else:
        return None


