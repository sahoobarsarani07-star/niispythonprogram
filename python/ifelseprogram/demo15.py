print("choose a shape to calculate area:")
print("1.square")
print("2.Rectangle")
print("3.circle")
choice=int(input("Enter your choice (1-3)"))
if choice ==1:
	side=float(input("Enter the side of the square:" ))
	area=side*side
	print("Area of Square=",area)
elif choice==2:
	length=float(input("Enter the length of the rectangle:"))
	breadth=float(input("Enter the breadth of the rectangle:"))
	area=length*breadth 
	print("Area of rectangle=",area)
elif choice==3:
	radius=float(input("Enter radius of the circle:"))
	area=math.pi*radius
	print("Area of circle=",area)
else:
	print("invalid choice")   