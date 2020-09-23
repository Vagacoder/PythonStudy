#
# * Pandas plot

#%%
# * Read air quality no 2 file
import pandas as pd 
import matplotlib.pyplot as plt 

# ? Set column 0 as index, and parse it to datetime
air_q = pd.read_csv('data/air_quality_no2.csv', index_col=0, parse_dates=True)

air_q.head()

# %%
# * using pandas built-in plot, for whole DataFrame

# ? DataFrame.plot.*
air_q.plot()

# %%
# * for Series

air_q['station_paris'].plot()
# %%
# * scatter plot

air_q.plot.scatter(x='station_london', y = 'station_paris', alpha=0.3)

# %%
# * list all built-in plot
[method_name for method_name in dir(air_q.plot) if not method_name.startswith('_')]

# %%
air_q.plot.box()

# %%
# * each column in separated subplot
axs = air_q.plot.area(figsize=(12, 8), subplots=True)

#%%
axs
# %%
