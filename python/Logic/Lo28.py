no = 121
s = 0
r = 0
temp = no

while no != 0:
    r = no % 10
    s = s * 10 + r
    no = no // 10   # fixed indentation

if temp == s:
    print(temp, "is pd number")
else:
    print(temp, "is not pd number")