#
# * Python Numpy Random Poisson
#%%
import numpy as np 
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sb 

sb.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

# %%
# * Normal and Poisson
sb.distplot(random.normal(loc=50, scale=7, size=1000), label='normal')
sb.distplot(random.poisson(lam=50, size=1000), label='poisson')
# %%
# * Binomial and Poisson
sb.distplot(random.binomial(n=1000, p=0.01, size=1000), label='binomial')
sb.distplot(random.poisson(lam=10, size=1000), label='poisson')

# %%
