#
# * Kaggle Course 02, Intro to Machine Learning
# * Using Pandas to Get Familiar With Your Data

# * Your first model (first half, data load and process)

#%%
# * import lib
import pandas as pd

# %%
# * load data, Melbourne Housing Snapshots
# ? download link: https://www.kaggle.com/dansbecker/melbourne-housing-snapshot

melbourne_file_path = '../data/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.shape)
melbourne_data.head()

# %%
# * stats of data
melbourne_data.describe()

#%%
# * view columns
melbourne_data.columns

# %%
# * There are some missing values, we drop them
melbourne_data = melbourne_data.dropna(axis=0)
melbourne_data

# %%
# * select column using dot notation
y = melbourne_data.Price
print(y.shape)
y

# %%
# * select column(s) using features
x = melbourne_data.drop('Price', axis=1)
print(x.shape)
x

# %%
# * all select columns using a list of col name (features)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = melbourne_data[melbourne_features]
print(x.shape)
x

# %%
# * stats of x
x.describe()

# %%
