alexa@ubuntu-xenial:0x00-linear_algebra$ cat 1-trim_me_down.py 
#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
for x in range(3) :
    the_middle.append(matrix[x][2:4])
print("The middle columns of the matrix are: {}".format(the_middle))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./1-trim_me_down.py 
The middle columns of the matrix are: [[9, 4], [7, 3], [4, 6]]
alexa@ubuntu-xenial:0x00-linear_algebra$ wc -l 1-trim_me_down.py 
6 1-trim_me_down.py
alexa@ubuntu-xenial:0x00-linear_algebra$ 
