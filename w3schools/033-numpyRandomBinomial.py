#
# * Python Numpy Random Binomial Distribution

#%%
import numpy as np 
import numpy.random as random
import matplotlib.pyplot as plt
import seaborn as sb

x = random.binomial(n=10, p=0.5, size=10)
print(x)

# %%
sb.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

# %%
# * difference between normal and binomial
sb.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sb.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show() 
# %%
# * Python Numpy Random Multinomial Distribution

y = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=3);

print(y)

