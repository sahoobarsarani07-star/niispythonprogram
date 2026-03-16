class VoterError(Exception):
    pass

print("Enter age:")
age = int(input())

try:
    if age >= 18:
        print("Eligible")
    else:
        raise VoterError("Age not allowed")

except VoterError:
    print("Not allowed")

print("Main end")