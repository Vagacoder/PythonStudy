#
# * Built-in data types

#%%
print(type('Hello'))
print(type(20))
print(type(20.5))

# * complex type
print(type(1j)) # get type
print(type(4+9j))
print((4+9j).conjugate())   # get conjugate
print(complex(2, 3))       # two to construct complex number
print(2+3j)

# * list
print(type(['applee', 'banana', 'cherry']))

# * tuple
print(type(('apple', 'banana', 'cherry')))

# * range
print(type(range(6)))

# * dictionary
print(type({'1':'apple', '2': 'banana', '3' : 'cherry'}))

# * set
print(type({'apple', 'banan', 'cherry'}))

# * frozen set
print(type(frozenset({'apple', 'banana', 'cherry'})))

# * bytes
print(type(b'Hello'))
print(b'Hello')

# * byte array
print(type(bytearray(5)))
print(bytearray(5))

# * memory view
print(type(memoryview(bytes(5))))
print(memoryview(bytes(5)))



