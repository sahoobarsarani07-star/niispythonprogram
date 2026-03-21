L=[5,8,6,6,3,8,7,7,12]
i=0
while i<len(L):
	if L[i]%2!=0:  #if odd
		L.remove(L[i])
	else:
		i+=1 #move only if not removed
print(L)
