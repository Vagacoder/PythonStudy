#
# * Numpy Array Join

#%%
import numpy as np

# * join 2 1d arrays
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

a31 = np.concatenate((a1, a2))
print(a31)
a32 = np.concatenate((a1, a2), axis=0)
print(a32)
try:
    a33 = np.concatenate((a1, a2), axis=1)
    print(a33)
except Exception as ex:
    print(ex)

# %%
# * join 2 2d arrays
a4 = np.array([[1, 2, 3],[4, 5, 6]])
a5 = np.array([[7, 8, 9],[10, 11, 12]])

print(a4.shape)
print(a5.shape)

a6 = np.concatenate((a4, a5), axis=0)
print(a6)

a7 = np.concatenate((a4, a5), axis=1)
print(a7)

# %%
# * stack 2 1d arrays

a8 = np.stack((a1, a2))
print(a8)

a9 = np.stack((a1, a2), axis=0)
print(a9)

a10 = np.stack((a1, a2), axis=1)
print(a10)

#%%
a11 = np.hstack((a1, a2))
print(a11)

a12 = np.vstack((a1, a2))
print(a12)

a13 = np.dstack((a1, a2))
print(a13)

# %%
