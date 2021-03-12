#!/usr/bin/env python3
  
import numpy as np

def np_slice(matrix, axes={}):
    result = []
    i = 0
    for key, value in axes.items():
        while i < key:
            result.append(slice(None))
            i += 1
        result.append(slice(*value))
        i += 1
    return matrix[tuple(result)]


