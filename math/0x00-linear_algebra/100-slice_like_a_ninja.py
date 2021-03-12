#!/usr/bin/env python3

import numpy as np

def np_slice(matrix, axes={}):
    result = []
    maxx = max(axes)
    for i in range(maxx + 1):
        if i in axes.keys():
            result.append(slice(*axes.get(i)))
        else:
            result.append(slice(None, None, None))
    return matrix[tuple(result)]


