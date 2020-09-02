#
# * Python Iterator

#%%
# * List, tuple, dictionary, set are all iterable class, whose objects have a 
# * iter() method to get an iterator.

dic1 = {'a': 1, 'b': 2, 'c': 3}
dic1Iter = iter(dic1)

print(next(dic1Iter))
print(next(dic1Iter))
print(next(dic1Iter))


# %%
# * String is also iterable objects

str1 = "Hello world"
str1Iter = iter(str1)

print(next(str1Iter))
print(next(str1Iter))
print(next(str1Iter))
print(next(str1Iter))


# %%
# * For customized iterable class, __init__() and __next__() are required
class MyNumbers:

    def __init__(self):
        self.a = 1


    def __iter__(self):
        return self


    # * to prevent iteration forever, we use StopIteration statement
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

    
numbers = MyNumbers()
numIter = iter(numbers)

print(next(numIter))
print(next(numIter))
print(next(numIter))
print(next(numIter))

for x in numIter:
    print(x)


# %%
