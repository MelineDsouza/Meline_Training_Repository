from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self,name) -> None:
        self.name = name

    @abstractmethod
    def speak(self):
        pass #an abtract method to be implemented in the child class


#Cannot create object for parent class,as it is abstract


class Dog(Animal):
    def speak(self):
        return f"{self.name}"



class cat(Animal):
    def speak(self):
        return f"{self.name}"

#we can create object for child classes

obj =cat("moss")
print(obj.speak())

obj1 = Dog("rocky")
print(obj1.speak())