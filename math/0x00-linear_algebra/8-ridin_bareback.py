#!/usr/bin/env python3

def mat_mul(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        result = []
        for i in range(len(mat1)):
            tmp = []
            for j in range(len(mat2[0])):
                n = 0
                for k in range(len(mat2)):
                    n += mat1[i][k] * mat2[k][j]
                tmp.append(n)
            result.append(tmp)
        for x in result:
            return result
    else :
        return None
