#
# * Train/Test
# ! Using sklearn

#%%
import numpy as np 
import matplotlib.pyplot as plt 

# * Generate dataset
np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

print(x)
print(type(x))
plt.scatter(x, y)
plt.show()

# %%
# * split into train/test
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# %%
# * plot training set
plt.scatter(train_x, train_y)
plt.show()
# %%
# * plot test set
plt.scatter(test_x, test_y)
plt.show()
# %%
# * Fit the data set
# ! increase order from 4 to 5, increase r^2 from 0.809 to 0.866
model1 = np.poly1d(np.polyfit(train_x, train_y, 4))

line1x = np.linspace(0, 6, 100)
line1y = model1(line1x)

plt.scatter(train_x, train_y)
plt.plot(line1x, line1y)
plt.show()

# %%
# * get r square of our model
from sklearn.metrics import r2_score

r2 = r2_score(test_y, model1(test_x))
print(r2)
# %%
# * predict
print(model1(5))
# %%
# * run on test

plt.scatter(test_x, test_y, label='Test')
plt.scatter(test_x, model1(test_x), label='Predict')
plt.plot(line1x, line1y)
plt.legend()
plt.show()
# %%
