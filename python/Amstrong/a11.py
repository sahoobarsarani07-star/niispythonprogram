r = int(input("Enter the number of terms: "))
a = 0
b = 1

if r >= 1:
    print(a, end=" ")
if r >= 2:
    print(b, end=" ")

count = 2
while count < r:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    count += 1
