d={1:"A",2:"B",4:"c",3:"E"}
print(d.keys())

d={1:"A",2:"B",4:"C",3:"C"}
print(d.keys())
print(d.values())
print(d.items())


d={1:"A",2:"B",4:"C",3:"C"}
for i in d.keys():
	print(i,d[i])


d={1:"A",2:"B",4:"C",3:"C"}
for k,v in d.items():
	print(k,v)


d={1:"A",2:"B",4:"C",3:"C"}
print(d[1])
#print(d[5])  error
print(d.get(1))
print(d.get(5))

d={}
d=d.fromkeys("welcome")


d={}
d=d.fromkeys("welcome")
print(d)
d1={}
d1=d1.fromkeys(range(5))
print(d1)