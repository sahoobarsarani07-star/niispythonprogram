s="welcome"
for i in range(len(s)-1,-1,-1):
	print(s[i])



s="welcome"
for i in range(-1,len(s)-1,-1):
	print(s[i])

s="welcome"
for i in s:
	print(i)

s="welcome"
s=s[::-1]
for i in s:
	print(i)

print(help(str))