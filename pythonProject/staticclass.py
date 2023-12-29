from datetime import date

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def age(name, age, birthyear):
        return name, date.today().year - birthyear

    @classmethod
    def age1(cls, name, age, birthyear):
        return name, date.today().year - birthyear

    def display(self):
        print(self.name, self.age)


# class child(people):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#
# staticchild = people.age("result1", 25, 1995)
# #staticchild.display()
# child_classmethod = people.age1("result2", 30, 1947)
# #child_classmethod.display()
#
# obj = people("mac", 15)
# print(obj.display())
#
#
#





