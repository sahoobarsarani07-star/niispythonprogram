#wap take emp salary from keyboard if sal>=5000,da=30%,hra=20%,then display basic salary da hra and total salary.
salary=float(input("enter basic salary:"))
if salary >=5000:
	da=salary*0.30  #30% DA
	hra=salary*0.20 #20% HRA
else:
	da=0
	hra=3
total=salary+da+hra
print("Basic salary=",salary)
print("DA=",da)
print("HRA=",hra)
print("Total salary=",total)
