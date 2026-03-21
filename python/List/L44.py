L = []

print("Enter how many lists to store:")
s = int(input())

for i in range(s):
    x = []
    print("Enter how many elements in list", i+1, ":")
    s1 = int(input())
    
    for j in range(s1):
        print("Enter element", j+1, ":")
        val = int(input())
        x.append(val)   # add element to sublist
    
    L.append(x)  # add sublist to main list

print("Elements are:")
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end="\t")
    print()