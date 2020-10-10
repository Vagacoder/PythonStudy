#
# * Kaggle Cousr 03, Intermediate Machine Learning
# * Missing Values


#%%
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split

# %%
# * Load data
X_full = pd.read_csv('../data/Iowa_housing_train.csv', index_col='Id')
print('X_full')
print(X_full.shape)
X_full

#%%
# *  check how many NaN in each columns
nanInCols = X_full.isnull().sum()
print(type(nanInCols))
nanInCols
for index in nanInCols.index:
    print('{} has {} NaN'.format(index, nanInCols[index]))

# %%
X_full['SalePrice'].isnull().sum()
#%%
X_test_full = pd.read_csv('../data/Iowa_housing_test.csv', index_col='Id')
print('X_test_full')
print(X_test_full.shape)
X_test_full

# %%
# * Remove rows with missing target
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
print('X_full, after drop NaN')
print(X_full.shape)
X_full

# %%
# * get target (SalePrice)
y = X_full.SalePrice
print(y.shape)
y
# %%
# * X_full remove target (SalePrice), leave only features
X_full.drop(['SalePrice'], axis=1, inplace=True)
print('X_full, after drop SalePrice')
print(X_full.shape)
X_full

# %%
# * To keep things simple, we'll use only numerical predictors
X = X_full.select_dtypes(exclude=['object'])
print('X, keep only numerical features')
print(X.shape)
X

# %%
X_test = X_test_full.select_dtypes(exclude=['object'])
print('X_test, keep only numerical features')
print(X_test.shape)
X_test

# * Break validatrion / Training
#%%
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8,
                                                    test_size=0.2, random_state=0)

# %%
X_train.head()

# %%
