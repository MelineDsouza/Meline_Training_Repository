from inheritance1 import Testing

#import from parent class

class child(Testing):
   #def __init__(self,a,b) -> None:
     #super().__init(a,b)

#---------or-----------

   def __init__(self) :
    Testing.__init__(self,4,5)


   def add2(self):
    return self.num2 + self.add()


obj = child()
print(obj.add2())

