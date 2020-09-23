#
# * Pandas Time series data

#%%
import pandas as pd 
import matplotlib.pyplot as plt

# * Note: here, we do not use 'parse_dates=['column name']' argument
air_q = pd.read_csv('data/air_quality_no2_long.csv')

air_q = air_q.rename(columns={'date.utc': 'datetime'})

air_q

# %%
air_q.city.unique()
# %%
# * here, we convert datetime from plaintext to datetime format
air_q['datetime']= pd.to_datetime(air_q['datetime'])

air_q['datetime']

# %%
# * find starting and ending time
air_q['datetime'].min(), air_q['datetime'].max()

# %%
# * find the time duration
air_q['datetime'].max() - air_q['datetime'].min()

# %%
air_q['month'] = air_q['datetime'].dt.month

air_q
# %%
air_q['datetime'].dt.weekday
# %%
air_q.groupby([air_q['datetime'].dt.weekday, air_q['location']])['value'].mean()

# %%
# * plot NO2 pattern during the day of all stations together
fig, axs = plt.subplots(figsize=(12, 4))
air_q.groupby([air_q['datetime'].dt.hour])['value'].mean().plot(
    kind='bar', rot=0, ax=axs
)

# %%
plt.xlabel('Hour of the day');
# %%
plt.ylabel('$NO_2 (ug/m^3)$');
# %%
air_q

# %%
no2 = air_q.pivot(index='datetime', columns='location', values='value')

no2
# %%
air_q.set_index('datetime')
# %%
no2.index.year, no2.index.weekday
# %%
no2['2019-05-20':'2019-05-21'].plot()
# %%
# ! Resample method: resample() is USEFULL!
monthlyMax = no2.resample('M').max()
monthlyMax
# %%
monthlyMax.index.freq
# %%
no2.resample('D').mean().plot(style='-o', figsize=(10,5))
# %%
