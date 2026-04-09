L=[0,0,0,0,0]
for i in range(0,len(L),1):
	print("enter element ",i+1)
	L[i]=int(input())
s=0
for i in L:
	s=s+i
print("sum of elemrnt=",s)