#
# * Python date time

#%%
import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.month)
print(x.day)

y = datetime.datetime(2020, 5, 17)
print(y)

# %%
print(x.strftime('%A'))
print(x.strftime('%a'))
print(x.strftime('%B'))
print(x.strftime('%b'))
print(x.strftime('%Y'))
print(x.strftime('%y'))
print(x.strftime('%X'))
print(x.strftime('%x'))
print(x.strftime('%M'))
print(x.strftime('%S'))
# %%
