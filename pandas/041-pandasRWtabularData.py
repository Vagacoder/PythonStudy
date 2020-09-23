#
# * Pandas Read/Write Tabular Data

# ? read_* and to_* for read/write files
# ? head()/tail() show data entries
# ? info() show summary

#%%
# * Load csv file using Pandas
import numpy as np
import pandas as pd
import sys, os

titanic = pd.read_csv('data/titanic_test.csv')

titanic
# %%
# * check first 8 rows
titanic.head(8)

# %%
# * check last 9 rows
titanic.tail(9)
# %%
# * column data type
titanic.dtypes

# %%
# * write DataFrame to Excel file
# ? read_* and to_* are paired

print(type(titanic))

titanic.to_excel('data/titanic_test.xlsx', sheet_name='passengers', index=False)

# %%
# * DataFrame info
# ! Important to know non-null/null entries
# titanic.describe()
titanic.info()
# %%
