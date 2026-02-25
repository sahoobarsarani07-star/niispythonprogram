#write a python program to reverse a 2-digit number.
print("enter 2-digit number")
n=int(input())
rev=(n%10)*10+(n//10)
print("reverse=",rev)
