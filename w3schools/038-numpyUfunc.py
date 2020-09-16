#
# * Python Numpy Ufunc

#%%
import numpy as np

print('Regular function [1,2,3] + [4,5,6]')

def add1(x, y):
    return x + y


print(add1([1,2,3],[4,5,6]))


print('Numpy universal function [1,2,3] + [4,5,6]')

add2 = np.frompyfunc(add1, 2, 1)

print(add2([1,2,3],[4,5,6]))

# %%
print(type(add2))
print(type(np.concatenate))

# %%
