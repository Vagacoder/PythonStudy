# 
# * Python Seaborn Matplotlib

#%%
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()


# %%
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

# %%
sns.distplot([0, 1, 2, 3, 4, 5, 3, 4, 2, 3, 3, 2 ,3, 1])
plt.show()
# %%
