import math
def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, int(math.sqrt(no)) + 1):
        if no % i == 0:
            return False
    return True
min = int(input("Enter a min range to max range\n "))
max = int(input())
s=0
for no in range(min,max+1,1):
	if is_prime(no):
	    print(no,end=" ")
	    s=s+no
print("\nsum=",s)