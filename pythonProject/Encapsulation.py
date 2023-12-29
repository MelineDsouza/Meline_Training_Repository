#wrapping of data and variables are declared in constructor and they are called in sub class

class Base:
    def __init__(self) ->None:
        self.a = "company"
        self._b = "Moolya"

class child(Base):
    def __init__(self) ->None:
        Base.__init__(self)
        #calling my private  member of class
        print(self._b)

obj=Base()
print(obj.a)
print(obj._b)