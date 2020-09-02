#
# * Dictionary

#%%
dic1 = {1: 'a', 'first': 23, 2: 'forty five', 'second': 'nice', 3: 99}
print(dic1)

print()

for x in dic1:
    print((x, dic1[x]))

print()

for val in dic1.values():
    print (val)

print()

for key, val in dic1.items():
    print('{1} : {0}'.format(val, key))

print()

dic1.popitem()
print(dic1)
dic1.pop(1)
print(dic1)
del dic1[2]
print(dic1)

print()

dic2 = dic1.copy()
print(dic2)



# %%
