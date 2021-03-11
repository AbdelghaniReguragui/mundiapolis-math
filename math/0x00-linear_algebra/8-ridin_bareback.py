alexa@ubuntu-xenial:0x00-linear_algebra$ cat 8-main.py
#!/usr/bin/env python3

def mat_mul(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        result = []
        for i in range(len(mat1)):
            tmp = []
            for j in range(len(mat2[0])):
                n = 0
                for k in range(len(mat2)):
                    n += mat1[i][k] * mat2[k][j]
                tmp.append(n)
            result.append(tmp)
        for x in result:
            return result
    else :
        return None

mat_mul = __import__('8-ridin_bareback').mat_mul

mat1 = [[1, 2],
        [3, 4],
        [5, 6]]
mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]
print(mat_mul(mat1, mat2))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./8-main.py
[[11, 14, 17, 20], [23, 30, 37, 44], [35, 46, 57, 68]]
alexa@ubuntu-xenial:0x00-linear_algebra$ 
