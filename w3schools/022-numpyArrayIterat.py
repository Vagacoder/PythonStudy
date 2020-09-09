#
# * Numpy array iterating

#%%
import numpy as np

a1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])

for x in a1:
    print(x)
    for y in x:
        print(y)


# %%
# * nditer()

for x in np.nditer(a1):
    print(x)


# %%
# * Iterating array with different data types

for x in np.nditer(a1, flags=['buffered'], op_dtypes=['S']):
    print(x)
    print(type(x))


# %%
for x in np.nditer(a1[:, ::2]):
    print(x)

# %%
b1 = np.array([1, 2, 3, 4])

for i, x in np.ndenumerate(b1):
    print(i, x)

b2 = a1.reshape(2, 2, 2)
for i, x in np.ndenumerate(b2):
    print(i, x)


# %%
