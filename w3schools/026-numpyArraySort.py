#
# * Python numpy array sort

#%%
import numpy as np

a1 = np.array([3, 5, 2, 4, 0, 1, 8, 7, 6])
a2 = np.sort(a1)
print(a1)
print(a2)

# %%
a3 = np.array(['banana', 'apple', 'kiwi', 'cherry'])
print(np.sort(a3))

# %%
a4 = np.array([True, False, False, True, False])
print(np.sort(a4))
# %%
# ! Note, for multi-d array, sort each array
a5 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(a5))
# %%
