import math

def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, int(math.sqrt(no)) + 1):
        if no % i == 0:
            return False
    return True

no = int(input("Enter a number: "))

if is_prime(no):
    print(no, "is a prime number")
else:
    print(no, "is not a prime number")