for no in range(10,21,1):
	c=0
	d=2
	if no==0 or no==1:
		continue

	while d<=no//2:
		if no%d==0:
			c=c+1
			break
		d=d+1
	if c==0:
		print(no," is prime number ")
print("enter min range to max range ")
min=int(input())
max=int(input())