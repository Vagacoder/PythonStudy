#
# * Multiple Regression 
# ! Using sklearn

#%%
# * Multiple regression is like linear regression, but with more than one independent 
# * value, meaning that we try to predict a value based on two or more variables.

import pandas

df = pandas.read_csv('data/cars.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

print(X)
print(y)
# %%
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(X, y)

# %%
# * Predict
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
# %%
# * Coefficient
# * find coefficient for Weight and Volume
print(regr.coef_)

print(regr.predict([[3300, 1300]]))
calculatedCof1 = (regr.predict([[3300, 1300]]) - regr.predict([[2300, 1300]]))/1000
print(calculatedCof1 - regr.coef_[0] < 1e5)
# %%
