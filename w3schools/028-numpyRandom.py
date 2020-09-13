#
# * Python Numpy Random

#%%
from numpy import random

for i in range(10):
    x = random.randint(100)
    print(x)


for i in range(10):
    y = random.rand()
    print(y)


# %%
x = random.randint(100, size=(5))
print(x)

y = random.randint(100, size=(3, 4))
print(y)

# %%
z = random.rand(5)
print(z)

w = random.rand(3, 4)
print(w)

# %%
u = random.choice([3, 5, 7, 9, 11, 13, 15, 17])
print(u)

v = random.choice([3, 5, 7, 9, 11, 13, 15, 17], size=(3, 4))
print(v)

# %%
