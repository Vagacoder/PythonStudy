#
# * Pandas, 10 min to Pandas guide 
# ? https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

#%%
import numpy as np 
import pandas as pd 

# %%
# ! Create Series, Note: the type of elements is float64
s1 = pd.Series([1, 3, 5, np.nan, 6, 8])
s1
# %%
# * Create DataFrame
dates = pd.date_range('20130101', periods=6, freq='1D')
dates
# %%
df1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df1
# %%
df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3]*4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test','train']),
    'F': 'foo'
})

df2
# %%
df2.dtypes
# %%
df2.A
# %%
# ! Viewing Data
df1.head()
# %%
df1.tail(3)
# %%
df1.index
# %%
# * cast Pandas Dataframe to Numpy arrays
df1.to_numpy()
# %%
# ? Dataframe with multiple dtype is expensive to cast to Numpy arrays
# ? since Numpy array is one dtype, it may cast every element to Object
df2.to_numpy()
# %%
# ! Quick statistic summary
df1.describe()

# %%
# * Transpose matrix
df1.T
# %%
# ! Sort by axis
# * axis = 1, row direction
df1.sort_index(axis=1, ascending=False)

# %%
# * axis = 0, column direction
df1.sort_index(axis=0, ascending=True)
# %%
# ! Sort by column name
df1.sort_values(by='B')
# %%
# !! Selection
# !! Recommend using access methods: .at() .iat() .loc() .iloc()
# ** select column by name
df1.A, df1['A'], df1[['A','B']]
#%%
# ! NOT work for column
df1.loc['A']
# %%
# * select rows using [index]
df1[0:3]
# %%
# * select rows using key
df1['20130102':'20130104']
# %%
# ** select row by label
print(dates[0])
df1.loc[dates[0]]
#%%
df1
# %%
# ! NOT work, [] only for column
df1[0]
#%%
# * Works for row
df1[0:1]
#%%
# * works for row
df1.iloc[0]
# %%
# ! NOT work, [] only for column
df1['20130102']
#%%
# * works for row
df1.loc['20130102']
# %%
# ! From single-axis label to multiple-axis label
df1.loc[dates[0]]

#%%
df1.loc[dates[0], ['A', 'B']]
#%%
df1.loc[:,['A', 'B']]

# %%
df1.loc['20130102':'20130104', ['A', 'B']]

# %%
# * get scalar value, single row, single col
df1.loc[dates[0], 'A']
# %%
# ! Note this is NOT scalar value
df1.loc[dates[0], ['A']]
# %%
# ** select by position
df1.iloc[3]
# %%
df1.iloc[3:5, 0:2]
# %%
df1.iloc[[1,2,4],[0,2]]
# %%
df1.iloc[1,1]
# %%
df1.iat[1,1]
# %%
# ! Boolean indexing
df1[df1['A'] > 0]
# %%
df1[df1 > 0]
# %%
df2 = df1.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df2
#%%
df2['E'].isin(['two', 'four'])
# %%
df2[df2['E'].isin(['two', 'four'])]
# %%
# ! Setting a new column aligns to data by the indices
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102',periods=6))
s1
# %%
df1['F'] = s1
# %%
df1
# %%
df1.at[dates[0], 'A'] = 0

# %%
df1.iat[0, 1] = 0
# %%
df1.loc[:, 'D'] = np.array([5]*len(df1))
# %%
df3 = df1.copy()

df3[df3 > 0]= -df3
# %%
df3
# %%
# ! Missing Data
df2 = df1.reindex(index=dates[0:4], columns=list(df1.columns) + ['E'])
# %%
df2
# %%
df2.loc[dates[0]:dates[1], 'E']=1 
# %%
df2
# %%
# * Drop N/A data
df2.dropna(how='any')
# %%
# * Fill N/A with daya
df2.fillna(value=88)
# %%
# * 