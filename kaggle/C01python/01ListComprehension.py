#
# * Kaggle, Course 01, Python
# * List Comprehension

#%%
# * simple
squares = [n**2 for n in range(10)]
print(squares)

# %%
# * a more complicated 
persons = ['Alex', 'Bob', 'Cindy', 'Dave', 'Eddy']
bigPerson = [p.upper() + ' BIG' for p in persons if len(p) > 3]
print(bigPerson)

# %%
# * special one
noPerson = ['no' for p in persons]
print(noPerson)
# %%
# * one line for sum, min, max, count
print(len([p for p in persons if len(p) >4]))

ns = [6, 3, 0, -2, 9, -7]
print(sum(n for n in ns if n > 0))
# %%
# ! Exercises
