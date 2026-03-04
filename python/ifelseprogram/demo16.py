print("Enter two numbers:")
no1=int(input("First number:"))
no2=int(input("second number:"))
print("\nEnter an operator(+,-,//):")
op=input("operator:")
if op =="+":
	print("Result=",no1 +no2)
elif op == "-":
	print("Result=",no1-no2)
elif op == "*":
	print("Result=",no1*no2)
elif op =="//":
  if no2 !=0:
  	print("Result=",no1//no2)
  else:
   print("Division by zero is not allowed.")
else:
	print("invalid operator")  