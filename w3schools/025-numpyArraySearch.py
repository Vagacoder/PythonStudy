#
# * Python Numpy Array Search

#%%
import numpy as np

a1 = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'c', 'd', 'c'])
i = np.where(a1 == 'c')

print(i)
print(type(i))
print(a1[i])

# %%
a2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
l = np.where(a2%2 == 0)
print(l)
print(a2[l])

# %%

# ! searchsorted() which performs a binary search in the array, and returns the 
# !index where the specified value would be inserted to maintain the search order.

m = np.searchsorted(a2, 4.5)
print(m)

n1 = np.searchsorted(a2, 7)
print(n1)

n2 = np.searchsorted(a2, 7, side='right' )
print(n2)

o = np.searchsorted(a2, [2, 4, 6])
print(o)

# %%
