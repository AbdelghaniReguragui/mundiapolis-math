#!/usr/bin/env python3
def summation_i_squared(n):
    #If n is not a valid number, return None
    if type(n) != int or n < 1:
        return None
    else:
        #if n > 1, do
        if n > 1:
            return n**2 + summation_i_squared(n-1)
        #when n == 1, return result
        return n
