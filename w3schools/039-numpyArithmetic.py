#
# * Python Numpy Arithmetic Function

#%%
import numpy as np 

a1 = [1,2,3]
a2 = [4,5,6]

print(a1 + a2)
print(np.add(a1, a2))

# %%
a3 = np.array([1,2,3])
a4 = np.array([4,5,6])

print(a3 + a4)
print(np.add(a3, a4))

# %%
# * Rounding decimals

a5 = [-3.1234, 3.745]
print(np.trunc(a5))
print(np.fix(a5))

# %%
a6 = [-3.15, -3.64, 3.2, 3.87]
print(np.around(a6))

# %%
