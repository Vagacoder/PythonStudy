#
# * Kaggle Course 02, Intro to Machine Learning
# * Your first model

#%%
import pandas as pd 
import numpy as np 

melbourne_file_path = '../data/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# %%
melbourne_data = melbourne_data.dropna(axis=0)
melbourne_data

# %%
y = melbourne_data.Price
print(y.shape)
y

# %%
x = melbourne_data.drop('Price', axis=1)
print(x.shape)
x

# %%
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print(x.shape)
X

# %%
X.describe()

#%%
X.head()

# %%
# * Build model from sklearn, scikit-learn.
# * 1 Decision tree model

from sklearn.tree import DecisionTreeRegressor

# * Define model. Specify a number fro random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# * Fit model
melbourne_model.fit(X, y)

# %%
# * try to predicate
print('Making predictions for the following 5 houses:')
print(X.head())
print('The predications are')
print(melbourne_model.predict(X.head()))
print('Actual price is:')
print(y.head())
# %%
