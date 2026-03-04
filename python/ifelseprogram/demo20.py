print("enter two numbers:")
a=int(input())
b=int(input())
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=int(input("Enter your choice:"))
match choice:
	case 1:
		print("Addition=",a+b)
	case 2:
		print("Subtraction=",a-b)
	case 3:
		print("Multiplication=",a*b)
	case 4:
		if b !=0:
			print("Division=",a/b)
		else:
			print("Cannot divide by zero")
     case_:
	    print("invalid choice") 
