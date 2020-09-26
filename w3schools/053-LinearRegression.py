#
# * Linear Regression

#%%
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def line(x):
    return slope*x + intercept


model1 = list(map(line, x))

print(model1)
# %%
x1 = 13
y1 = line(13)
print(y1)

plt.scatter(x, y)
plt.plot(x, model1)
plt.scatter(x1, y1, marker='o')

plt.xlabel('x')
plt.ylabel('y')
plt.title('r: {}'.format(r))
plt.show()

# %%
