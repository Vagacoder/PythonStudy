#
# * Python file handling

#%%
# * file read
try:
    f = open('./data/d1.txt', 'rb')
    content = f.read()
    print(content)
except:
    print('File is not found!')
finally:
    f.close()

f = open('./data/d1.txt', 'rt')
content = f.read(6)
print(content)
f.close()

f = open('./data/d1.txt', 'rt')
print(f.readline())
print(f.readline())
f.close()

f = open('./data/d1.txt', 'rt')
for x in f:
    print(x)
f.close()

# %%
# * file append
f = open('./data/da1.txt', 'at')
f.write('Add a new line after original file\n')
f.close()

# %%
# * file write
f = open('./data/dw1.txt', 'wt')
f.write('New line\n')
f.close()

# %%
# * create file
f = open('./data/dnew1.txt', 'x')
f.write('New line in new file\n')
f.close()

# %%
# * delete a file
import os
filename = './data/dnew1.txt'
if os.path.exists(filename):
    os.remove('./data/dnew1.txt')
else:
    print('No {}'.format(filename))

# %%
# * create and delte folder
import os
foldername = './data/subfolder/'
if not os.path.exists(foldername):
    os.mkdir(foldername)
else:
    print('Folder {} exists'.format(foldername))

if os.path.exists(foldername):
    os.rmdir(foldername)
else:
    print('Folder {} does not exist'.format(foldername))

# %%
# * with statement
with open('./data/d1.txt', 'rt') as d1:
    content = d1.readline()
    print(content)
    for line in d1:
        print(line)


# %%
