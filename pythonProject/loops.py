sum=0
for i in range(1,6):
    sum= sum+i
    print(i,sum)

i=1
while i<6:
    print(i)
    i+=1


num=0
for number in range(10):
    if number==5:
        break
    print(number)

    num=0
for number in range(10):
    if number==5:
        continue
     print(number)


  #  if else
a=10
b=5
c=20
if a>b and a>c:
    print("a is greater",a)
elif b>c and b>a:
    print("b is greater",b)
else:
    print("c is greater")
