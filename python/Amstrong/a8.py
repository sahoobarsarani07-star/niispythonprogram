def find_armstrong_in_range(limit):
    """Finds and prints all Armstrong numbers from 1 to limit."""
    for no in range(1, limit + 1):
        p = len(str(no))
        temp = no
        arm = 0
        while temp != 0:
            r = temp % 10
            arm += r ** p
            temp //= 10
        if arm == no:
            print(no, "is an Armstrong number")

# Main program: Call the function only once
r = int(input("Enter a range: "))
find_armstrong_in_range(r)

