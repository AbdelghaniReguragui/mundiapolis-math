alexa@ubuntu-xenial:0x00-linear_algebra$ cat 4-main.py 
#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    if (len(arr1) == len(arr2)):
        arr = []
        for x in range(len(arr2)):
            arr.append(arr1[x]+arr2[x])
        return arr
    else :
        return None

add_arrays = __import__('4-line_up').add_arrays

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./4-main.py 
[6, 8, 10, 12]
[1, 2, 3, 4]
[5, 6, 7, 8]
None
alexa@ubuntu-xenial:0x00-linear_algebra$ 
