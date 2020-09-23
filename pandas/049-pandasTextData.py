#
# * Pandas, Handle textual data

#%%
import pandas as pd 

titanic = pd.read_csv('data/titanic.csv')

titanic
# %%
# * make all names lower case
# * .str is accessor
titanic['Name'].str.lower()

# %%
# * split name string
titanic['Name'].str.split(',')

# %%
# * add surname column
titanic['Surname'] = titanic['Name'].str.split(',').str.get(0)

titanic['Surname']
# %%
titanic['Name'].str.contains('Countess')
titanic[titanic['Name'].str.contains('Countess')].count()
    
# %%
titanic[titanic['Name'].str.contains('Countess')]['Name']
# %%
# * longest name
titanic['Name'].str.len(), \
    titanic['Name'].str.len().idxmax(),\
        titanic['Name'][titanic['Name'].str.len().idxmax()],\
            titanic.loc[titanic['Name'].str.len().idxmax(), ['Name']]

# %%
# * replace values in columns
titanic['Sex_s'] = titanic['Sex'].replace({'male':'M', 'female':'F'})

titanic['Sex_s']

# %%
