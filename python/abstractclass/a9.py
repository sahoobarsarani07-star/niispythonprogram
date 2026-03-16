print("main start")
L=[10,20,30]
try:
	print(L[2]//2)
except IndexError as e:
	print("hi",e)
except ZeroDivisionError as e:
	print("bye",e)
	print("main end")