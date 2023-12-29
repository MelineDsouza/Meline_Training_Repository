class Testing:
    num = 100  # global variable

    #contructor
    def __init__(self, a, b) -> None:
        self.firstvalue = a
        self.secondvalue = b
        print("im am contructor")

    def data(self):
        print("python session is going on")

    def add(self):
        return self.firstvalue + self.secondvalue + Testing.num

        # create an object


obj = Testing(4, 5)
obj.data()
print(obj.add())

obj1 = Testing(10, 10)
obj1.data()
print(obj1.add())
