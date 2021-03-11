alexa@ubuntu-xenial:0x00-linear_algebra$ cat 10-main.py 
#!/usr/bin/env python3

def np_shape(matrix):
        return matrix.shape

import numpy as np
np_shape = __import__('10-ill_use_my_scale').np_shape

mat1 = np.array([1, 2, 3, 4, 5, 6])
mat2 = np.array([])
mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
print(np_shape(mat1))
print(np_shape(mat2))
print(np_shape(mat3))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./10-main.py 
(6,)
(0,)
(2, 2, 5)
alexa@ubuntu-xenial:0x00-linear_algebra$
