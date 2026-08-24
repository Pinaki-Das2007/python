# np.insert(array,index,values,axix= none)
# array - original array
# index - index before which values is inserted
# values - values to be inserted
# axis - axis along which values is inserted, if axis is none, array is flattened first


import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr) # [10 20 30 40 50 60]
new_arr = np.insert(arr,2,100,axis=None)
print(new_arr) # [ 10  20 100  30  40  50  60]