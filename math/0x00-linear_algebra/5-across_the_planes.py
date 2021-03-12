#!/usr/bin/env python3

def add_matrices2D(mat1, mat2):
    if (len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])):
        result = []
        for x in range (len(mat1)):
            tmp = []
            for y in range (len(mat1[0])):
                print ("y = ",y,"\n")
                tmp.append(mat1[x][y] + mat2[x][y])
            result.append(tmp)
        return result
    else:
        return None
