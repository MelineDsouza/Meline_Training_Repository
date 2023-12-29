from staticclass import people

class Child(people):
    name=('sunil')

print(Child.age('sunil',15,1998))
print(Child.age1('mac',28,1988))