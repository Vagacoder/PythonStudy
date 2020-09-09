#
# * Numpy data types

#%%
import numpy as np

a1 = np.array([1, 2, 3, 4])
print(a1.dtype)

a2 = np.array(['apple', 'banana', 'cherry'])
print(a2.dtype)

# %%
a3 = np.array([1, 2, 3, 4], dtype='S')
print(a3.dtype)
print(a3)

a4 = np.array([1, 2, 3, 4], dtype='i4')
print(a4.dtype)
print(a4)

# %%
a5 = np.array([1.1, 1.2, 1.3])

a6 = a5.astype(int)
print(a5)
print(a6)
print(a6.dtype)

a7 = np.array([1, 0, 3])
a8 = a7.astype(bool)
print(a8)
print(a8.dtype)

# %%
