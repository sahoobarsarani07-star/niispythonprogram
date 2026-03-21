L=[]
print("enter howmany list store")
s=int(input())
for i in range(0,s,1):
	x=[]
	print("enter list data")
	x=eval(input())
	L.append(x)
print("elements are")
for i in range(0,len(L[i]),1):
	for j in range(0,len(L[i]),1):
		print(L[i][j],end="\t")
	print()
