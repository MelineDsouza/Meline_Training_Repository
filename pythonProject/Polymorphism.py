class Dog:
    def Sound(self):
        print("bow bow")

    def Color(self):
        print("color of dog is brown")




class Cat():
    def Sound(self):
        print("meow meow")

    def Color(self):
        print("color of dog is white")




obj_dog = Dog()
obj_cat = Cat()

obj_dog.Sound()
obj_dog.Color()
obj_cat.Sound()
obj_cat.Color()

#
# for Animal in (obj_dog, obj_cat):
#     Animal.Sound()
#     Animal.Color()
