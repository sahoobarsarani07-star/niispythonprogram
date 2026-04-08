d={1:"A",2:"B",4:"C",3:"C"}
#print(d.set default(5))
#print(d)
print(d.setdefault(6,"F"))
print(d)



d={1:"A",2:"B"}
d1=d.copy()
print(d)
print(d1)


d={}
print(type(d))


d={}
d[1]="A"
d[2]="B"
print(d)


d={}
d[1]="A"
d[2]="B"
d[1]="C"
print(d)


d={1:"A",3:"B",2:"C"}
print(d)
print(d[3])


d={1:"A", True:"B",3:"C",3:"D"}
print(d)
