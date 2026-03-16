print("main start")
L=[10,20,30]
try:
	print(L[3])
except IndexError as e:
	print(e)
print("main end")