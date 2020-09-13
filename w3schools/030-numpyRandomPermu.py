#
# * Numpy Random Permutation

#%%
import numpy as np
# from numpy import random

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([1, 2, 3, 4, 5])

np.random.shuffle(a2)

print(a2)

# %%
print(np.random.permutation(a1))

print(a1)
# %%
