#
# * Pandas Reshape tables\
# TODO: This is advanced method, come back later

#%%
import pandas as pd 

try:
    titanic = pd.read_csv('data/titanic_test.csv')
    air_q = pd.read_csv('data/air_quality_long.csv', index_col='date.utc', parse_dates=True)
except Exception as ex:
    print(ex)
    
titanic.head()
air_q.head()

# %%
# * sort titanic data according to class and age descending order
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()

#%%
# * Long to wide table format
no2 = air_q[air_q['parameter'] == 'no2']

no2 
# %%
no2_subset = no2.sort_index().groupby(['location']).head(2)

no2_subset
# %%
no2_subset.pivot(columns='location', values='value')
# %%
