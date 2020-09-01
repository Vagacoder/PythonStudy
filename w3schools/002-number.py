#
# * Numbers

#%%
# * Basic number types
print('1. Basic number types')
x = 1
y = 2.8
z = 1+2j

print(float(x))
print(complex(x))
print(int(y))
print(complex(y))

# ! cannot cast complex to int or float, even imagery part is 0
# print(int(z)) 
# print(float(z))
# print(int(complex(1, 0)))

#%%
# * Random Numbers

import random
print('\n2. Random numbers')
print(random.randrange(1, 10))

#%%
# * Type casting

print('\n3. Type casting')
print(str(x))
print(str(y))
print(str(z))
# %%
