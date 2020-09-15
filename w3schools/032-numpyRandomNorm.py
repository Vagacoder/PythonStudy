#
# * Python Random Normal distribution

#%%
import numpy as np 
from numpy import random
import matplotlib.pyplot as pl
import seaborn as sb

x = random.normal(size=(10))
print(x)
sb.distplot(x)
pl.show()

# %%
y = random.normal(size=(3,5))
print(y)
sb.distplot(y)
pl.show()

# %%
z = random.normal(loc=1, scale=2, size=(2,3))
print(z)
sb.distplot(z)
pl.show()

# %%
sb.distplot(random.normal(size=1000))
pl.show()

# %%
