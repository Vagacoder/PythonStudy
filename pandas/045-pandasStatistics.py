#
# * Pandas Statistics 

#%%
# * Load csv file
import pandas as pd 

titanic = pd.read_csv('data/titanic_test.csv')
titanic.head()

# %%
# * mean of column
ageMean = titanic['Age'].mean()
print('Mean of age column is: {}'.format(ageMean))

# %%
# * median, multiple columns 
ageMedian = titanic[['Age', 'Fare']].median()
print('Median of age column is: {}, median of fare is: {}'.format(ageMedian[0], ageMedian[1]))

# %%
# * describe cross multiple column
titanic[['Age', 'Fare']].describe()

# %%
# * self defined aggregating statistics
titanic.agg({
    'Age': ['min', 'max', 'median', 'skew'],
    'Fare': ['min', 'max', 'median', 'skew']
})
# %%
# ! USEFULL! groupby()
# * aggregating groups by category
# ? subdata is 2 columns, groupby() applies to Sex column, then mean() to each group
titanic[['Sex', 'Age']].groupby('Sex').mean()

#%%
# ? Another way, not good as above
titanic.groupby('Sex')['Age'].mean()
# %%
titanic.groupby('Sex').mean()

#%%
titanic[['Pclass','Fare']].groupby('Pclass').mean()

#%%
# * Multiple group
titanic.groupby(['Sex', 'Pclass'])['Fare'].mean()

# %%
# * count number
titanic['Pclass'].value_counts()
# %%
