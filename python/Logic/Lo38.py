#small  element
L=[5,7,9,2,6]
small=L[0]
for i in range(1,len(L),1):
	if small>L[i]:
		small=L[i]
print("small element =",small)