#!/usr/bin/env python3

def cat_matrices2D(mat1,mat2,axis=0):
    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        tmp1 = [x[:]for x in mat1]
        tmp2 = [x[:]for x in mat2]
        result = tmp1 + tmp2
        return result
    elif(len(mat1) == len(mat2)) and axis == 1:
        result = [mat1[x] + mat2[x]for x in range(len(mat1))]
        return result
    else:
        return None
