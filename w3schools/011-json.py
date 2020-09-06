#
# * Pythono json

#%%
import json

x = '{ "name": "John", "age": 30, "city":"Here"}'
print(x)
print(type(x))

obj1 = json.loads(x)
print(obj1)
print(type(obj1))
print(obj1["name"])

z = json.dumps(obj1)
print(z)
print(type(z))

print(json.dumps('hello'))
print(json.dumps(42))
print(json.dumps(42.2))
print(json.dumps(True))
print(json.dumps(None))
print(json.dumps((42, 51)))

person1 = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

pd1 = json.dumps(person1, indent=2, separators=(".", " = "))
print(pd1)
print(type(pd1))

pd2 = json.dumps(person1, indent=2, separators=(".", " = "), sort_keys=True)
print(pd2)
print(type(pd2))

# ! But your may not convert this formated string back to json object
print(json.loads(pd2))

# %%
# ! can Not dumpt python object to string
class Obj:

    def __init__(self):
        self.number = 123
        self.name = 'obj'


obj2 = Obj()

print(obj2)
print(json.dumps(obj2))

# %%
