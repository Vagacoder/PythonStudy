#
# * Python pickle

#%%
import pickle

person1 = {
    'name': 'Alex',
    'age': 30,
    'pay': 4000.0,
    'vacation': False
}

person2 = {
    'name': 'Bob',
    'age': 25,
    'pay': 2518.50,
    'vacation': True
}

database = {}

database['person1'] = person1
database['person2'] = person2

with open('./data/persons.pkl', 'wb') as pickleFile:
    pickle.dump(database, pickleFile)
    print('Database of person is saved!')

# %%
import pickle

with open('./data/persons.pkl', 'rb') as readPickleFile:
    data = pickle.load(readPickleFile)
    for key in data.keys():
        print(key, end=':\n')
        for (k, v) in data[key].items():
            print('\t{}: {}'.format(k, v))

    

# %%
print(data)
# %%
