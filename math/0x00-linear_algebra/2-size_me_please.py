#!/usr/bin/env python3
"""
dsfa fdsad abjn a  bhd iywg ighwjq mka 0osqn kerl khe pjad hujfee oiewqn hwrekqjn eqwhijleq
"""
def matrix_shape(matrix):
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
