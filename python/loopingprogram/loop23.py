def print_into(**kwargs):
	for key,value in kwargs.items():
		print(f"{key}:{value}")
#calling with varing keyword arguments.
print_info(name="Alice",age=30,city="New York")
