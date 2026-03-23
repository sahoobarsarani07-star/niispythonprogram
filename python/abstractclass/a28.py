def divide(no1,no2):
	print("divide start")
	try:
		print(no1/no2)
	except:
		print("caught")
		print("divide end")
print("main start")
divide(10,2)
divide(10,0)
print("main end")