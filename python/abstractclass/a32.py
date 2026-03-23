class NegativeError(Exception):
    def __init__(self):
        print("Negative number not allowed")

print("enter a number")
no = int(input())

try:
    if no < 0:
        raise NegativeError()
    else:
        print("number =", no)
except NegativeError:
    print("Exception caught: negative number not allowed")

print("program end")