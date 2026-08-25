"""
np.concatenate() is used to join two or more arrays of the same shape along a specified axis. It takes a sequence of arrays as input and returns a new array that contains all the elements from the input arrays concatenated together.
np.concatenate((array1,array2),axis = 0)
axis = 0 means that the arrays will be joined along the first axis (vertically).
axis = 1 means that the arrays will be joined along the second axis (horizontally).
"""


import numpy as np
arr1 = np.array([1, 2,3])
arr2 = np.array([4, 5, 6])

new_arr = np.concatenate((arr1, arr2), axis=0)
print(new_arr)