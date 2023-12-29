a={10,20,30,40,40,50}
print(a)

b=set((10,20,30,40))
print(b)
print(len(a))

#difference
c=a.symmetric_difference(b)
print(c)

#common in both
n=c=a.intersection(b)
print(n)

m=a.difference(b)
print(m)

#combine both
o=a.union(b)
print(o)

p=a.add(b)
print(p)

q=a.remove(b)
print(q)
