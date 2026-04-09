#find second small  element
L = [5,4,3,2,1]
small = float('inf')
ssmall= float('inf')
for i in range(0,len(L),1):
	if small>L[i]:
		ssmall=small
		small=L[i]
	if small>L[i] and L[i]<ssmall:
		ssmall=L[i]
print(" small element =",small)
print("second small element =",ssmall)