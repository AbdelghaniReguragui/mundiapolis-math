#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    if(len(arr1) == len(arr2)):
        arr = []
        for x in range(len(arr2)):
            arr.append(arr1[x]+arr2[x])
        return arr
    else:
        return None
