alexa@ubuntu-xenial:0x00-linear_algebra$ cat 6-main.py 
#!/usr/bin/env python3

def cat_arrays(arr1, arr2):
    return arr1 + arr2

cat_arrays = __import__('6-howdy_partner').cat_arrays

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8]
print(cat_arrays(arr1, arr2))
print(arr1)
print(arr2)
alexa@ubuntu-xenial:0x00-linear_algebra$ ./6-main.py 
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5]
[6, 7, 8]
alexa@ubuntu-xenial:0x00-linear_algebra$ 
