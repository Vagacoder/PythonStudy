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
# * get boolean mask for nan
pd.isna(df2)
# %%
# ! Basic Statics Operations
df1
#%%
# * mean of column, axis = 0
df1.mean()
#%%
# * mean of row, axis = 1
df1.mean(1)
# %%
s1 = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
s1
# %%
df1.sub(s1, axis='index')
# %%
# ! Apply function to data
df1.apply(np.cumsum)
# %%
df1.apply(lambda x: x.max()-x.min())
# %%
# ! Histogramming
s2 = pd.Series(np.random.randint(0, 7, size=10))
s2
# %%
s2.value_counts()
# %%
# ! String methods
s3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s3.str.lower()
# %%
# ! Merge
# * Concat
df4 = pd.DataFrame(np.random.randn(10, 4))
df4
# %%
# * break into pieces
pieces = [df4[:3], df4[3:7], df4[7:]]
pieces
# %%
# * concatenate
pd.concat(pieces)
# %%
# * Join
left = pd.DataFrame({'key':['foo','foo'], 'lval': [1,2]})
right = pd.DataFrame({'key': ['foo','foo'], 'rval': [4, 5]})

# %%
left
# %%
right
# %%
pd.merge(left, right, on='key')
# %%
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
# %%
left
# %%
right
# %%
pd.merge(left, right, on='key')
# %%
# ! Grouping
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                        'foo', 'bar', 'foo', 'foo'],
                 'B': ['one', 'one', 'two', 'three',
                      'two', 'two', 'one', 'three'],
                'C': np.random.randn(8),
                'D': np.random.randn(8)})

df
# %%
df.groupby('A').sum()
# %%
# * same as above
df[['A','C', 'D']].groupby('A').sum()
# %%
df.groupby(['A', 'B']).sum()
# %%
# ! Reshape
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                 'foo', 'foo', 'qux', 'qux'],
                 ['one', 'two', 'one', 'two',
                  'one', 'two', 'one', 'two']]))

# %%
tuples
# %%
index = pd.MultiIndex.from_tuples(tuples, names=['first','second'])
#%%
index
# %%
df = pd.DataFrame(np.random.randn(8,2), index=index, columns=['A', 'B'])
df2 = df[:4]
df2
# %%
# ! Stack: “compresses” a level in the DataFrame’s columns.
stacked = df2.stack()
# %%
stacked
# %%
stacked.unstack()
# %%
stacked.unstack(1)
# %%
stacked.unstack(0)
# %%
# ! Pivot tables
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                 'B': ['A', 'B', 'C'] * 4,
                 'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                 'D': np.random.randn(12),
                 'E': np.random.randn(12)})
# %%
df
# %%
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
# %%
# ! Time Series
# * initial data is every second
rng = pd.date_range('1/1/2012', periods=100000, freq='S')

# %%
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

# %%
ts.resample('5Min')
# %%
# * resample to every 5 minutes
ts.resample('5Min').sum()
# %%
# ! Time zone representation
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')

# %%
ts = pd.Series(np.random.randn(len(rng)),rng)
# %%
ts
# %%
# * set time zone to UTC
ts_utc = ts.tz_localize('UTC')
ts_utc
# %%
# * different time zone
ts_utc.tz_convert('US/Eastern')
# %%
rng = pd.date_range('1/1/2012', periods=5, freq='M')
# %%
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# %%
ts
# %%
# * to time span
ps=ts.to_period()
# %%
ps
# %%
# * back to time stamp
ps.to_timestamp()
# %%
#! Categoricals
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'raw_grade': ['a', 'b', 'b', 'a', 'a', 'e']
    
})
# %%
df['grade'] = df['raw_grade'].astype('category')
# %%
df['grade']
# %%
df['grade'].cat.categories=['very good', 'good', 'very bad']
# %%
df
# %%
df['grade']= df['grade'].cat.set_categories(['very bad', 'bad', 'medium', 'good', 'very good'])
# %%
df.sort_values(by='grade')
# %%
df.groupby('grade').size()

# %%
# ! Plotting
import matplotlib.pyplot as plt 
plt.close('all')
# %%
ts = pd.Series(np.random.randn(1000),
                index=pd.date_range('1/1/2000', periods=1000))
# %%
ts = ts.cumsum()
# %%
ts.plot()

# %%
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
# %%
df.plot()
# %%
df.cumsum().plot()
# %%
# ! Get data in/out
# ! to csv file
df.to_csv('data/dfoo1.csv')
# %%
# ! to HDF5 file
df.to_hdf('data/dfoo1.h5','df')
# %%
df1 = pd.read_csv('data/dfoo1.csv')
df1
# %%
df2 = pd.read_hdf('data/dfoo1.h5','df')
df2
# %%
