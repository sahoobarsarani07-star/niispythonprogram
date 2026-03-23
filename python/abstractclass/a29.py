def divide(no1,no2):
	print("divide start")
	print(no1/no2)
	print("divide end")
print("main start")
divide(10,2)
try:
	divide(10,0)
except:
	print("exception handle")
print("main end")
