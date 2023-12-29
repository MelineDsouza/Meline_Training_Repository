class python:
    #CONSTRUCTOR
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def display(self):
        print("my name is",self.name)
        print("my age is",self.age)

obj = python("mac","28")
obj.display()






#protected
class python:
    #CONSTRUCTOR
    def __init__(self,name,age) -> None:
        self._name = name
        self._age = age

    # protected method
    def display(self):
        print("my name is",self._name)
        print("my age is",self._age)

obj = python("sunil","25")
obj.display()









#private
class python:
    #CONSTRUCTOR
    def __init__(self,name,age) -> None:
        self.__name = name
        self.__age = age

#private  method
    def __display(self):
        print("my name is",self.__name)
        print("my age is",self.__age)

obj = python("amal","30")
obj._python__display()