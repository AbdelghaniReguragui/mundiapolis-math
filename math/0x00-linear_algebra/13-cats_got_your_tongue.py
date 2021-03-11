alexa@ubuntu-xenial:0x00-linear_algebra$ cat 13-main.py
#!/usr/bin/env python3

def np_cat(mat1, mat2, axis=0):
    return np.concatenate((mat1, mat2), axis=axis)

import numpy as np
np_cat = __import__('13-cats_got_your_tongue').np_cat

mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])
mat3 = np.array([[7], [8]])
print(np_cat(mat1, mat2))
print(np_cat(mat1, mat2, axis=1))
print(np_cat(mat1, mat3, axis=1))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./13-main.py
[[11 22 33]
 [44 55 66]
 [ 1  2  3]
 [ 4  5  6]]
[[11 22 33  1  2  3]
 [44 55 66  4  5  6]]
[[11 22 33  7]
 [44 55 66  8]]
alexa@ubuntu-xenial:0x00-linear_algebra$ 
