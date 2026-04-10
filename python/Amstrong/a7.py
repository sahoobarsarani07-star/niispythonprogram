# Main program to check all numbers in the range
r = int(input("Enter a range: "))
for no in range(1, r + 1):
    if is_armstrong(no):
        print(no, "is an Armstrong number")
