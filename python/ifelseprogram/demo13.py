#wap take no from keyboard number is divisible by 5 abd 7 only 7 not divisible 5 and 7.
print("enter a number")
no=int(input())
if no%5==0 and no%7==0:
	print("d by 5 and 7")
elif no%7==0:
	print("only 5")
elif no%7==0:
	print("only 7")
else:
	print("not div by 5 and 7")