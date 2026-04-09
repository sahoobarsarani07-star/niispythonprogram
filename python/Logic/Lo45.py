
for i in range(68,64,-1):
	for j in range(68,i-1,-1):
		print(chr(j),end="\t")
	print()


for i in range(65,69,1):
	for j in range(i,64,-1):
		print(chr(j),end="\t")
	print()


for i in range(68,64,-1):
	for j in range(i,64,-1):
		print(chr(j),end="\t")
	print()


for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(i%2,end="\t")
	print()


for i in range(1,5,1):
	for j in range(1,i+1,1):
		print((i+1)%2,end="\t")
	print()


for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(j%2,end="\t")
	print()


for i in range(1,5,1):
	for j in range(1,i+1,1):
		print((j+1)%2,end="\t")
	print()



for i in range(1,5,1):
	for j in range(1,i+1,1):
		print((i+j)%2,end="\t")
	print()


for i in range(1,5,1):
	for j in range(1,i+1,1):
		print((i+j+1)%2,end="\t")
	print()


for i in range(1,5,1):
	for j in range(1,i+1,1):
		if i%2==0:
			print("#",end="\t")
		else:
			print("@",end="\t")
	print()


c=0
for i in range(1,5,1):
	for j in range(1,i+1,1):
		c=c+1
		print(c,end="\t")
	print()


c=1
c1=0
for i in range(1,5,1):
	for j in range(1,i+1,1):
		c1=c+i
		if i%2==0:
			c1=c1-1
			print(c1,end="\t")
		else:
			print(c,end="\t")
		c=c+1
	print()





for i in range(1,5,1):
	for j in range(1,i+1,i):
		print(j,end="")
	print("1")


for i in range(1,5,1):
	for j in range(1,i+1,i):
		print(j,end="")
	for j in range(i,0,-1):
		print(j,end="")
	print()

for i in range(1,5,1):
	for j in range(1,i+1,i):
		print(j,end="")
	for j in range(i,0,-1):
		print(j,end="")
	print()
for i in range(4,0,-1):
	for j in range(1,i+1,i):
		print(j,end="")
	for j in range(i,0,-1):
		print(j,end="")
	print()

   
for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	print()
  

for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")	
	print()

for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")	
	print()
for i in range(4,0,-1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")	
	print()


for i in range(4,0,-1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")	
	print()
for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")	
	print()



for i in range(68,64,-1):
	for j in range(68-i,0,-1):
		print(end=" ")
	for j in range(65,i+1,1):
		print(chr(j),end="")
	for j in range(i,64,-1):
		print(chr(j),end="")
	print()

s="welcome"
for i in range(0,len(s),1):
	for j in range(0,i+1,1):
		print(s[j],end="")
	print()