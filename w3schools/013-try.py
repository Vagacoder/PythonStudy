#
# * Python try except 

#%%
try:
    print(x)
except NameError:
    print('x is not found')
except:
    print('Something wrong')
finally:
    print('block 1 is done')

try:
    print('hello')
except:
    print('something wrong')
else:
    print('everything is good')
finally:
    print('block 2 is done')

try:
    f = open('data/d1.txt', 'r')
    content = f.read()
    print(content)
    print('d1.txt is read')
except:
    print('Cannot read d1.txt')
finally:
    f.close()
    print('d1.txt is closed')

try:
    f = open('../data/p1.txt', 'r')
    content = f.read()
    print(content)
    print('p1.txt is read')
except:
    print('Cannot open ../data/p1.txt')
finally:
    f.close()
    print('p1.txt is closed')


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
    finally:
        print('Exception handled')


x = -1
if not type(x) is str:
    raise Exception('Type error') from TypeError


# %%
