#
# * Numpy Random Distribute

#%%
from numpy import random

a1 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
x = random.choice(a1, p=[0.05, 0.1, 0.1, 0.15, 0.2, 0.15, 
        0.1, 0.1, 0.05], size=(50))
print(x)

# %%
a2 = [3, 5, 7, 9]
y = random.choice(a2, p=[0.1, 0.3, 0.6, 0.0], size=(4,7))
print(y)

# %%
