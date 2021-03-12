#!/usr/bin/env python3

def matrix_transpose(matrix):
    a = []
    for i in range(len(matrix[0])):
        b = []
    for j in range(len(matrix)):
        b.append(matrix[j][i]) 
        a.append(b)
    return a
