L=[10,5,7,6]
try:
	print(L[4]/0)
except IndexError:
	print("index error")
except ZeroDivisionError:
	print("zero division error")
except:
	print("handle all type")
print("program end")