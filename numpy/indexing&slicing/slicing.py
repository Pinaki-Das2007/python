# arra[start:stop:step] - slicing
# in step if you are not entering anything it will take default value as 1
# negetive idexx(-1) will start from the end and will go to the start of the array. It mean it will reverse the array.



import numpy as np

arr = np.array([10, 20, 30, 40, 50,60])
print(arr[1:5]) #index from 1 to 4
print(arr[:4]) #index from 0 to 3
print(arr[::2]) # every second element
print(arr[::-1])
