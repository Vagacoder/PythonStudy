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
print(nanInCols)

print()

for index in nanInCols.index:
    print('{} has\t\t{} NaN'.format(index, nanInCols[index]))

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
print('X_full, after drop NaN in SalePrice column')
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
# ? Step 1 Preliminary investigation
# * check X_train and X_valid
print(X_train.shape)
X_train.head()

# %%
print(X_valid.shape)
X_valid.head()

# %%
# * Number of missing values in each column of training data
missing_val_count_by_column = (X_train.isnull().sum(axis=0))
missing_val_count_by_column
# %%
print(missing_val_count_by_column[missing_val_count_by_column > 0])
# %%
# ! Since each column has 1168 rows, we miss 212, 6 and 58 rows, its not worth to drop whole column
# * do imputation
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# * Function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# %%
# ? Step 2 Drop column with missing values

col_missing_values = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']
reduced_X_train = X_train.drop(col_missing_values, axis=1)
reduced_X_train
# %%
reduced_X_valid = X_valid.drop(col_missing_values, axis=1)
reduced_X_valid
# %%
# * get MAE on droped X_train and X_valid
print("MAE (Drop columns with missing values):")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

# %%
# ? Step 3 Imputation
# * part A

from sklearn.impute import SimpleImputer
imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(imputer.transform(X_valid))

imputed_X_train
# %%
imputed_X_valid
# %%
# * During imputation, columns names are removed, get them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns 

# %%
# * get MAE on imputed X_train and X_valid
print("MAE (Imputation):")
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))

# %%
# * part B
# TODO

#%%
# ? Step 4 Generate test predictions
# * part A
# * we pick drop columns
final_X_train = reduced_X_train
final_X_valid = reduced_X_valid

# %%
# * Define and fit model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(final_X_train, y_train)
# %%
preds_valid = model.predict(final_X_valid)
print('MAE (my way):')
print(mean_absolute_error(y_valid, preds_valid))

# %%
# * part B
final_X_test = pd.DataFrame(imputer.transform(X_test))
final_X_test.columns = X_test.columns
final_X_test = final_X_test.drop(col_missing_values, axis=1)
print(final_X_test.shape)

# %%
preds_test = model.predict(final_X_test)
preds_test
# %%
