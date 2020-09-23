#
# * Python Pandas Basic

# ? DataFrame
# ? Series
# ? DataFrame.describe()

#%%
import numpy as np
import pandas as pd

# * DataFrame
# * DataFrame is orgnized in columns
df = pd.DataFrame({
    'Name':['Alex', 'Bob', 'Charlie'],
    'Age': [21, 35, 58],
    'Sex': ['male', 'male', 'male']
})

df

#%%
# * Series
# * Each column in DataFrame is a Series
df['Name']

#%%
# * Create a Series
ages = pd.Series([18, 21, 19], name='Age')

ages

#%%
# * Operations on DataFrame
df['Age'].max()

# %%
# * Operation on Series
ages.max()

# %%
# * Basic statistic info of DataFrame
df.describe()

# %%
