#big  element
L=[5,7,9,6]
big=L[0]
for i in range(1,len(L),1):
	if big<L[i]:
		big=L[i]
print("big element =",big)
