#uples are used to store multiple items in a single variable
a=(10,"sunil",True,20,"Banglore","sunil")
b=("chennai","hydrabad","Delhi")
print(a)
print(b)
print(type(a))
print(len(a))
print(a[3])
print(a.count('sunil'))
print(a.index(True))
c=a+b
print(c)
print(*a,*b)

for i in a:
    print(i)

    #range
print(a[0:4])
