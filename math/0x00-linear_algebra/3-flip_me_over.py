#!/usr/bin/env python3

def matrix_transpose(matrix):
    tmp = []
    for x in range(len(matrix[0])):
        b = []
        for y in range(len(matrix)):
            b.append(matrix[y][x])
        tmp.append(b)
    return tmp
