#
# * Python Numpy Exponential Distribution

#%%
import numpy as np 
import numpy.random as random
from matplotlib import pyplot as plt 
import seaborn as sb

x = random.exponential(scale=2, size=(2,3))
print(x)

#%%
sb.distplot(random.exponential(size=1000))
plt.show()

# %%
# * Chi Square Distribution

y = random.chisquare(df=2, size=(3,4))

print(y)
sb.distplot(random.chisquare(df=1, size=1000))
plt.show()

# %%
