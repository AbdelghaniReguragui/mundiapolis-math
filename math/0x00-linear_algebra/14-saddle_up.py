alexa@ubuntu-xenial:0x00-linear_algebra$ cat 14-main.py
#!/usr/bin/env python3

import numpy as np

def np_matmul(mat1, mat2):
    result = np.dot(mat1, mat2)
    return result

np_matmul = __import__('14-saddle_up').np_matmul

mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat3 = np.array([[7], [8], [9]])
print(np_matmul(mat1, mat2))
print(np_matmul(mat1, mat3))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./14-main.py
[[ 330  396  462]
 [ 726  891 1056]]
[[ 550]
 [1342]]
alexa@ubuntu-xenial:0x00-linear_algebra$ 
