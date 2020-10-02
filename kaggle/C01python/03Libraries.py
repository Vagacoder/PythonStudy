#
# * Kaggle Course 01, Python

#%%
from numpy.core.defchararray import narray
import tensorflow as tf
import numpy as np

rolls = np.random.randint(low=1, high=7, size=10)
print(type(rolls))
print(rolls)

# %%
list1 = [[1,2,3],[4,5,6]]
narray1 = np.asarray(list1)

print(list1)
print(narray1)
print(list1[1][-1])
print(narray1[1][-1])
print(narray1[1, -1])
# print(list1[1, -1])

# %%
a = tf.constant(1)
b = tf.constant(1)
print(a+b)
# %%
list1.__add__(3)
# %%
narray1.__add__(3)
# %%
l1 = [1,2,3]
l1.__contains__(4)
# %%
