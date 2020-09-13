#
# * Python Numpay Array Split

#%%
import numpy as np

# * split 1d arrays
a1 = np.array([1, 2, 3, 4, 5, 6])

a2 = np.array_split(a1, 3)
print(a2)

a3 = np.array_split(a1, 4)
print(a3)

# %%
# * split 2d arrays
a4 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

a5 = np.array_split(a4, 3)
print(a5)

a6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

a7 = np.array_split(a6, 3)

print(a7) 

# %%
a8 = np.array_split(a6, 3, axis=1)
print(a8)

a9 = np.hsplit(a6, 3)
print(a9)

# %%
