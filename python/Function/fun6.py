def sical():
	print("enter principle")
	P=float(input())
	print("enter rate of interest")
	R=float(input())
	print("enter time")
	T=float(input())
	SI=(P*R*T)/100
	return SI
res=sical()
print("simple interest",res)