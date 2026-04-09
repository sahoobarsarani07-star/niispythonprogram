#divide two number without floor division operator   and also find remainer

no1=2
no2=3

q=0

while no1>=no2:
	q=q+1
	no1=no1-no2
print("q=",q)
print("remainder=",no1)
