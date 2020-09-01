#
# * Boolean 

#%%
print('1. Only empty string, list, tuple, set, dic and number 0 is False')

print(bool('False'))
print(bool(''))
print(bool([1, 2, 3]))
print(bool([]))
print(bool((1, 2)))
print(bool(()))
print(bool({1, 2}))
print(bool(set()))
print(bool({'1': 1, '2': True}))
print(bool({}))
print(bool(-1))
print(bool(0))


#%%
print('\n2. Any object with method __len__ which returns 0, is False')

class Example:

    def __init__(self, length=0):
        self.length = length

    
    def __len__(self):
        return self.length

    
ex0 = Example(0)
ex1 = Example(1)

print(len(ex0))
print(len(ex1))
print(bool(ex0))
print(bool(ex1))

# %%
