# it tells how many axes/dimensions does this numpy array have
# it returns an integer value

import numpy as np

arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)
print(arr_3d)