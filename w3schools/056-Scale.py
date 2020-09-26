#
# * Scale Features
# ! Using sklearn.preprocessing

#%%
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

# * tranformer
scale = StandardScaler()

df = pandas.read_csv('data/cars.csv')

X = df[['Weight', 'Volume']]
print(X)

# %%
# * standarization  newX = (x - mean)/stdev
scaledX = scale.fit_transform(X)
print(scaledX)

# %%
# * train model and predict

y = df['CO2']

regModel = linear_model.LinearRegression()
regModel.fit(scaledX, y)

# ? transform input
scaledInput = scale.transform([[2300, 1.3]])

predictedCO2 = regModel.predict([scaledInput[0]])
print(predictedCO2)

# %%
