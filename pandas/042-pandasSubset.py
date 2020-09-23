#
# * Pandas How to select subset/column

#%%
import pandas as pd 

titanic = pd.read_csv('data/titanic_test.csv')

titanic.head()
# %%
# * Select column
ages = titanic['Age']

ages.head()

# %%
# * Column in DataFrame is a Series
type(ages)

# %%
# * check the dimensional info of Series
ages.shape

#%%
# * check the dimensional info of DataFrame
titanic.shape

# %%
# * select multiple columns
age_sex = titanic[['Age', 'Sex']]

age_sex.head()
# %%
# * multiple column is a DataFrame
type(age_sex)
# %%
# * check shape
age_sex.shape

# %%
# * How to filter specific rows from a DataFrame

above_35 = titanic[titanic['Age'] > 35]

above_35.head()

#%%
# * how it works, Series > 35 returns a Series of boolean
titanic['Age'] > 35

#%%
# * How to filter from a range
class_23 = titanic[titanic['Pclass'].isin([2,3])]

class_23
# %%
# * boolean Series
titanic['Pclass'].isin([2,3])

# %%
# * boolean Seris, alternative expression
(titanic['Pclass'] == 2) | (titanic['Pclass'] == 3)

# %%
# * How to filter not N/A
age_no_na = titanic[titanic['Age'].notna()]

age_no_na
# %%
age_no_na.shape

#%%
# * Combine filter and multi selection
# ! in this case [] is not enough, need loc()/iloc()
# ! for name, using loc()
adult_name = titanic.loc[titanic['Age'] > 35, ['Name', 'Sex']]

adult_name
# %%
# * using slice operator
# ! for index, using iloc()
titanic.iloc[9:12, 2:5]
# %%
