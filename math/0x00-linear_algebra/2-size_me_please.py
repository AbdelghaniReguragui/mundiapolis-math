#!/usr/bin/env python3
''' la fonction matrix_shape prend comme parametres une matrice'''
def matrix_shape(matrix):
    ''' si la matrice ne contient qu'une seule ligne ca retourne la longueur de la ligne '''
    if type(matrix[0]) is not list:
        return [len(matrix)]
    ''' sinon  ca calcul le nombre de ligne + colonne '''
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
