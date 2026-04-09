L=[]
print("enter how many  element to store ")
n=int(input())
for i in range(0,n,1):
	print("enter element ",i+1)
	L.append(int(input()))
s=0
for i in L:
	s=s+i
print("sum of elemrnt=",s)