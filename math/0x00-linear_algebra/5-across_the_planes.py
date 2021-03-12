#!/usr/bin/env python3

def add_matrices2D(mat1, mat2):
    if (len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])):
        result = []
        for i in range (len(mat1)):
            tmp = []
            for j in range (len(mat1[0])):
                tmp.append(mat1[i][j] + mat2[i][j])
            result.append(tmp)
        return result
    else:
        return None
