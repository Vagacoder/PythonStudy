#
# * Python Regular Expression

#%%
import re

txt = 'The rain in Spain'
regex1 = '^The.*Spain$'
x = re.search(regex1, txt)

print(x)
print(x.start())

if(x):
    print('Yes')
else:
    print('No')

regex2 = 'The Spain'
y = re.search(regex2, txt)

print(y)

z = re.findall(regex1, txt)
print(z)

regex3 = 'a|i'
w = re.findall(regex3, txt)
print(w)

u = re.split('\s', txt)
print(u)

v = re.split('\s', txt, 1)
print(v)

t = re.sub('\s', '@', txt)
print(t)

t = re.sub('\s', '@', txt, 2)
print(t)
# %%
