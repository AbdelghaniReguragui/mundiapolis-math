alexa@ubuntu-xenial:0x00-linear_algebra$ cat 102-main.py
#!/usr/bin/env python3

def matrix_shape(matrix):
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])


def concat_recursive(mat1, mat2, axe):
    result = []
    if axe == 0:
        result = mat1 + mat2
        return result
    for i in range(len(mat1)):
        result.append(concat_recursive(mat1[i], mat2[i], axe - 1))
    return result


def cat_matrices(mat1, mat2, axis=0):
    if len(matrix_shape(mat1)) > axis and len(matrix_shape(mat2)) > axis:
        return concat_recursive(mat1, mat2, axis)
    else:
        return None

import numpy as np
import time
cat_matrices = __import__('102-squashed_like_sardines').cat_matrices

mat1 = [1, 2, 3]
mat2 = [4, 5, 6]
np_mat1 = np.array(mat1)
np_mat2 = np.array(mat2)

t0 = time.time()
m = cat_matrices(mat1, mat2)
t1 = time.time()
print(t1 - t0)
print(m)
t0 = time.time()
np.concatenate((np_mat1, np_mat2))
t1 = time.time()
print(t1 - t0, "\n")

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
np_mat1 = np.array(mat1)
np_mat2 = np.array(mat2)

t0 = time.time()
m = cat_matrices(mat1, mat2)
t1 = time.time()
print(t1 - t0)
print(m)
t0 = time.time()
np.concatenate((np_mat1, np_mat2))
t1 = time.time()
print(t1 - t0, "\n")

t0 = time.time()
m = cat_matrices(mat1, mat2, axis=1)
t1 = time.time()
print(t1 - t0)
print(m)
t0 = time.time()
np.concatenate((mat1, mat2), axis=1)
t1 = time.time()
print(t1 - t0, "\n")

mat3 = [[[[1, 2, 3, 4], [5, 6, 7, 8]],
         [[9, 10, 11, 12], [13, 14 ,15, 16]],
         [[17, 18, 19, 20], [21, 22, 23, 24]]],
        [[[25, 26, 27, 28], [29, 30, 31, 32]],
         [[33, 34, 35, 36], [37, 38, 39, 40]],
         [[41, 42, 43, 44], [45, 46, 47, 48]]]]
mat4 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
         [[19, 110, 111, 112], [113, 114 ,115, 116]],
         [[117, 118, 119, 120], [121, 122, 123, 124]]],
        [[[125, 126, 127, 128], [129, 130, 131, 132]],
         [[133, 134, 135, 136], [137, 138, 139, 140]],
         [[141, 142, 143, 144], [145, 146, 147, 148]]]]
mat5 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
         [[117, 118, 119, 120], [121, 122, 123, 124]]],
        [[[125, 126, 127, 128], [129, 130, 131, 132]],
         [[141, 142, 143, 144], [145, 146, 147, 148]]]]
np_mat3 = np.array(mat3)
np_mat4 = np.array(mat4)
np_mat5 = np.array(mat5)

t0 = time.time()
m = cat_matrices(mat3, mat4, axis=3)
t1 = time.time()
print(t1 - t0)
print(m)
t0 = time.time()
np.concatenate((np_mat3, np_mat4), axis=3)
t1 = time.time()
print(t1 - t0, "\n")

t0 = time.time()
m = cat_matrices(mat3, mat5, axis=1)
t1 = time.time()
print(t1 - t0)
print(m)
t0 = time.time()
np.concatenate((np_mat3, np_mat5), axis=1)
t1 = time.time()
print(t1 - t0, "\n")

m = cat_matrices(mat2, mat5)
print(m)
alexa@ubuntu-xenial:0x00-linear_algebra$ ./102-main.py
1.6927719116210938e-05
[1, 2, 3, 4, 5, 6]
4.76837158203125e-06 

1.8358230590820312e-05
[[1, 2], [3, 4], [5, 6], [7, 8]]
3.0994415283203125e-06 

1.7881393432617188e-05
[[1, 2, 5, 6], [3, 4, 7, 8]]
6.9141387939453125e-06 

0.00016427040100097656
[[[[1, 2, 3, 4, 11, 12, 13, 14], [5, 6, 7, 8, 15, 16, 17, 18]], [[9, 10, 11, 12, 19, 110, 111, 112], [13, 14, 15, 16, 113, 114, 115, 116]], [[17, 18, 19, 20, 117, 118, 119, 120], [21, 22, 23, 24, 121, 122, 123, 124]]], [[[25, 26, 27, 28, 125, 126, 127, 128], [29, 30, 31, 32, 129, 130, 131, 132]], [[33, 34, 35, 36, 133, 134, 135, 136], [37, 38, 39, 40, 137, 138, 139, 140]], [[41, 42, 43, 44, 141, 142, 143, 144], [45, 46, 47, 48, 145, 146, 147, 148]]]]
5.030632019042969e-05 

0.00020313262939453125
[[[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]], [[17, 18, 19, 20], [21, 22, 23, 24]], [[11, 12, 13, 14], [15, 16, 17, 18]], [[117, 118, 119, 120], [121, 122, 123, 124]]], [[[25, 26, 27, 28], [29, 30, 31, 32]], [[33, 34, 35, 36], [37, 38, 39, 40]], [[41, 42, 43, 44], [45, 46, 47, 48]], [[125, 126, 127, 128], [129, 130, 131, 132]], [[141, 142, 143, 144], [145, 146, 147, 148]]]]
1.5735626220703125e-05 

None
alexa@ubuntu-xenial:0x00-linear_algebra$ 
