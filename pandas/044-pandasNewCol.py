#
# * Pandas, New Column

#%%
import pandas as pd

air_q = pd.read_csv('data/air_quality_no2.csv', index_col=0, parse_dates=True)

air_q.head()

# %%
# * append a new column
air_q['london_mg_per_cubic'] = air_q['station_london']*1.882

air_q.head()

# %%
#
air_q['ratio_paris_antwerp'] = air_q['station_paris'] / air_q['station_antwerp']

air_q
# %%
# * make a new DataFrame and rename columns
air_q_new = air_q.rename(columns={
    'station_antwerp':'ant',
    'station_paris': 'paris',
    'station_london':'london'
})

air_q_new
# %%
