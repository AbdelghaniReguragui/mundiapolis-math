alexa@ubuntu-xenial:0x00-linear_algebra$ cat 5-main.py 
#!/usr/bin/env python3

def add_matrices2D(mat1, mat2):
    if (len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])):
        result = []
        for x in range (len(mat1)) :
            tmp = []
            for y in range (len(mat1[0])):
                print ("y = ",y,"\n")
                tmp.append(mat1[x][y] + mat2[x][y])
            result.append(tmp)
        return result
    else :
        return None

add_matrices2D = __import__('5-across_the_planes').add_matrices2D

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./5-main.py 
[[6, 8], [10, 12]]
[[1, 2], [3, 4]]
[[5, 6], [7, 8]]
None
alexa@ubuntu-xenial:0x00-linear_algebra$ 
