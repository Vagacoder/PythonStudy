#
# * Python Numpy Logisitic Distribution

#%%
import numpy as np
from numpy import random
import matplotlib.pyplot as pt
import seaborn as sb

x = random.logistic(loc=1, scale=2, size=(4,7))
print(x)
# %%
sb.distplot(random.logistic(size=1000))
pt.show()

# %%
# * Normal and Logistic distribution

sb.distplot(random.normal(scale=2, size=1000), label='normal')
sb.distplot(random.logistic(size=1000), label='logistic')
pt.show()

# %%
