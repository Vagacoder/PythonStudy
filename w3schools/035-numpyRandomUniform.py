#
# * Python Numpy Uniform 

#%%
import numpy as np 
from numpy import random

import matplotlib.pyplot as pt
import seaborn as sb

x = random.uniform(size=(2, 3))
print(x)
# %%
sb.distplot(random.uniform(size=1000))
pt.show()

# %%
