# rehsape(rows, columns)
#  we can do reshape when it is dimension match
# it never create a copy , it just returns the view of the original array



import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)