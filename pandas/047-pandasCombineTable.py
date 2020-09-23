#
# * Pandas combine data from multiple tables

#%%
import pandas as pd 

air_q = pd.read_csv('data/air_quality_no2_long.csv', parse_dates=True)
air_q_no2 = air_q[['date.utc', 'location','parameter', 'value']]
air_q_no2.head()

# %%
air_q_pm = pd.read_csv('data/air_quality_pm25_long.csv', parse_dates=True)
air_q_pm = air_q_pm[['date.utc', 'location', 'parameter', 'value']]
air_q_pm.head()

# %%
# * combine 2 tables of NO2 and PM
air_q = pd.concat([air_q_pm, air_q_no2], axis=0)
air_q

# %%
print(air_q_pm.shape)
print(air_q_no2.shape)
print(air_q.shape)

#%%
air_q = air_q.sort_values('date.utc')
air_q
# %%
# * combine without designate column
air_q1 = pd.concat([air_q_pm, air_q_no2], keys=['PM25','NO2'])
air_q1

# %%
# TODO: merge()
