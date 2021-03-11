alexa@ubuntu-xenial:0x00-linear_algebra$ cat 7-main.py 
#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        tmp1 = [x[:] for x in mat1]
        tmp2 = [x[:] for x in mat2]
        result = tmp1 + tmp2
        return result
    elif (len(mat1) == len(mat2)) and axis == 1:
        result = [mat1[x] + mat2[x] for x in range(len(mat1))]
        return result
    else:
        return None

cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)
print(mat4)
print(mat5)
mat1[0] = [9, 10]
mat1[1].append(5)
print(mat1)
print(mat4)
print(mat5)
alexa@ubuntu-xenial:0x00-linear_algebra$ ./7-main.py 
[[1, 2], [3, 4], [5, 6]]
[[1, 2, 7], [3, 4, 8]]
[[9, 10], [3, 4, 5]]
[[1, 2], [3, 4], [5, 6]]
[[1, 2, 7], [3, 4, 8]]
alexa@ubuntu-xenial:0x00-linear_algebra$ 
