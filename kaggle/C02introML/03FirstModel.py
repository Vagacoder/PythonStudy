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
x = melbourne_data[melbourne_features]
print(x.shape)
x

# %%
x.describe()

# %%
# * Build model from sklearn
