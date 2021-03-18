#!/usr/bin/env python3
#La matrice '''
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
#La boucle for
for x in range(3):
    # il prend x[2], x[3] de chaque ligne '''
    the_middle.append(matrix[x][2:4])
print("The middle columns of the matrix are: {}".format(the_middle))
