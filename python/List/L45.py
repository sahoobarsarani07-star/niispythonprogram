L=[[0,0,0],[0,0,0]]
print("enter",len(L)*len(L[0]),"elements")
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
		L[i][j]=int(input())
print("elements are")
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
		print(L[i][j],end="\t")
	print()