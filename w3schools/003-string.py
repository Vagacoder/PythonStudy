#
# * String

#%%
print('1. Multiline strings, it keeps all new lines')
a = '''This 
is a good
 example 
 to test space
if you like.'''

print(a)
# %%
print('\n2. String as arrays')
a = 'This is an example'
for i in range(len(a)):
    print(a[i], end=', ')
print()

# %%
print('\n3. Slicing string and negative indexing')
print(a[2:6])
print(a[-6: -1])
print(a[2: -1])

# %%
print('\n4. Strip the white space from beginning and ending of string')
b = '\thello world! \n'
print(b.strip())

# %%
print('\n5. Split string using deliminater')
c = ',hello, world, you are, welcome, '
print(c.split(',', 3))
# %%
print('\n6. Check strings')
txt = 'The rain in Spain stays mainly in the plain'
print('ain' in txt)

# %%
print('\n7. String format')
age = 36
txt1 = 'I am {}'
print(txt1.format(age))

number = 100
price = 4.95
print('I am {2}, buy {0} apples at price of {1:2.2f}'
        .format(number, price, age)) 
      
# %%
print('\n8. Other string methods')
b = 'hello world!'
print(b)
print(b.center(20))
print(b.ljust(20), 'this at right side')


# %%
