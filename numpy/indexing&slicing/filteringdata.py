#  filetering data means boolean masking
import numpy as np

arr = np.array([10, 20, 30, 40, 50,60])

print(arr[arr>25]) #filtering data which is greater than 25
