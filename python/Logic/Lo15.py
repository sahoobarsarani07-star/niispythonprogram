def  checkprime(no):
	c=0
	d=2
	if no==0 or no==1:
		return 1
	while d<=no//2:
		if no%d==0:
			c=c+1
		d=d+1
	return c
print("enter a number ")
no=int(input())
if checkprime(no)==0:
	print(no,"is prime number ")
else:
	print(no,"is not  prime number ")
