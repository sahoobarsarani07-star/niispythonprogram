#wap to take emp salary from keyboard if sal>=5000 da=30% hra=30% hra=20% if sal<5000 da=20% hr=10% then display basic salary da hra and total sal.
print("enter basic salary")
sal=float(input())
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
else:
	da=sal*0.2
	hra=sal*0.1
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)