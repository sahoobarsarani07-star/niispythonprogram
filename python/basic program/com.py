#write a python program to calculate compound interest.
print("enter principal")
P=float(input())
print("enter rate")
r=float(input())
print("enter time")
t=float(input())
print("enter number of times compounded")
n=int(input())
CI=P*(1+r/n)**(n*t)-P
print("compound interest=",CI)
