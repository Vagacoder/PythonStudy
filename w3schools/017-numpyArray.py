#
# * numpy array

#%%
import numpy as np

print(np.__version__)

print('\nNumpy 0d array, Scalar, Elements in array')
a1 = np.array(42)
print(type(a1))
print(np.ndim(a1))
print(a1)

print('\nNumpy 1d array')
a2 = np.array([1, 2, 3, 4, 5])
print(type(a2))
print(np.ndim(a2))
print(a2)

print('\nNumpy 2d array, Matrix, 2nd order Tensor')
a3 = np.array([[1, 2, 3], [4, 5, 6]])
print(type(a3))
print(a3.ndim)
print(a3)

print('\nNumpy nd array')
a4 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(type(a4))
print(np.ndim(a4))
print(a4)
# %%
print('\nAccess element')
a5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a5[0,1,2])
print(a5[0][1][2])

print(a5[1, -1, -2])
# %%
print('\nSlice array')
print(a2)
print(a2[1: 4])
print(a2[:4])
print(a2[1:])
print(a2[:])
print(a2[1:-1])
print(a2[::2])

a6 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(a6)
print(a6[1, 1:4])
print(a6[:, 2])
print(a6[:1, 2:5])
# %%
