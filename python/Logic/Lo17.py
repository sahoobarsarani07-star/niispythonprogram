import math
def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, int(math.sqrt(no)) + 1):
        if no % i == 0:
            return False
    return True
min = int(input("Enter a min range: "))
max = int(input("Enter a max range: "))
for no in range(min,max+1,1):
	if is_prime(no):
	    print(no, "is a prime number")