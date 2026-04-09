import sys
no=int(input("enter a number \n"))
c=0
d=2
if no==0 or no==1:
	print(no," ids not prime number ")
	sys.exit()
while d<=no//2:
	if no%d==0:
		c=c+1
		break
	d=d+1
if c==0:
	print(no," is prime number ")

else:
	print(no," is not prime number ")
