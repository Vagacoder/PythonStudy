#
# * Numpy Array Copy and View

#%%
import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
x = a1.copy()
y = a1.view()
z = a1

print('Original arrays')
print(a1)
print(x)
print(y)

print('\nUpdate copy')
x[0] = 42
print(a1)
print(x)
print(y)

print('\nUpdate view')
y[1] = 99
print(a1)
print(x)
print(y)

print('\nCheck base')
print(a1.base)
print(x.base)
print(y.base)
print(z.base)

# %%
