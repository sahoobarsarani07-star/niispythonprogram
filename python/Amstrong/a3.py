#using function armstrong number 
def count_digits(n):
    """Returns the number of digits in n."""
    return len(str(n))

def is_armstrong(n):
    """Checks if a number is an Armstrong number."""
    p = count_digits(n)
    temp = n
    arm = 0
    while temp != 0:
        r = temp % 10
        arm += r ** p
        temp //= 10
    return arm == n