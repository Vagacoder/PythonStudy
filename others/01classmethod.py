#
# * Decorator: @classmethod

#%%
class Student(object):

    student_id = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # * you can update student_id like below
        Student.student_id += 1


    @classmethod
    def fromStr(cls, name):
        firstName, lastName = map(str, name.split(' '))
        
        # * cls is uninitiated class
        student = cls(firstName, lastName)
        cls.student_id += 1
        return student


    @staticmethod
    def setFromStr(name):
        return [x for x in map(str, name.split(' '))]


    
print(Student.student_id)
scott = Student.fromStr('Scott Bernad')
print(type(scott))
print(scott.first_name)
print(scott.last_name)
print(Student.student_id)

Student.setFromStr('Alex Bob')

# %%
