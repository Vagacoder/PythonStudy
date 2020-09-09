#
# * Numpy Array Shape

#%%
import numpy as np

a1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a1)
print(a1.shape)

a2 = np.array([1, 2, 3, 4], ndmin=5)
print(a2)
print(a2.shape)


# %%
a3 = a1.reshape(4,2)
print(a3)
print(a3.shape)

try:
    a4 = a1.reshape(3, 4)
    print(a4)
    print(a4.shape)
except ValueError as err:
    print(err)


# %%
try:
    a5 = a1.reshape(2, 2, 2)
    print(a5)
    print(a5.shape)

    print('\na5 base is: ', end='')
    print(a5.base)

    a5[0, 0, 0] = 99
    print('\nAfter modify, a1 is: \n', end='')
    print(a1)
    print('\nAfter modify, a5 is: \n', end='')
    print(a5)
except:
    pass

# %%
try:
    a6 = a1.reshape(4, -1)
    print(a6)
    print(a6.shape)
except:
    pass


# %%
print(a1)

a7 = a1.reshape(-1)
print(a7)

a8 = a1.flatten()
print(a8)

# %%
