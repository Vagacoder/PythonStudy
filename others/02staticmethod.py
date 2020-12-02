#
# * Decorator: @staticmethod

#%%
class Person:
    @staticmethod
    def greet():
        print("Hello!")


# * static method can be called from Class or Instance
Person.greet()
p1 = Person()
p1.greet()

# %%
