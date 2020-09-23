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
# TODO https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/05_add_columns.html
