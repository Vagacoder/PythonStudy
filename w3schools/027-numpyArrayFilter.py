#
# * Python Numpy Array Filter

#%%
import numpy as np

a1 = np.array([41, 42, 43, 44])
mask1 = np.array([True, False, True, False])
a2 = a1[mask1]
print(a2)

# %%
mask2 = []

for x in a1:
    if x > 42:
        mask2.append(True)
    else:
        mask2.append(False)

print(a1[mask2])

# %%
mask3 = a1 > 42
print(a1[mask3])

# %%
print(a1[a1%2 == 0])
# %%
