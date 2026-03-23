class NegativeError(BaseException):
	def init(self):
		print("negative number not allow")
print("enter a number")
no=int(input())
if no<0:
	raise NegativeError()
else:
	print("number=",no)
print("program end")