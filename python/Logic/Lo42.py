#find second big  element
L = [5,4,3,2,1]
big = float('-inf')
sbig = float('-inf')
for i in range(0,len(L),1):
	if big<L[i]:
		sbig=big
		big=L[i]
	if big>L[i] and L[i]>sbig:
		sbig=L[i]
print(" big element =",big)
print("second big element =",sbig)