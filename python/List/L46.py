L = []
print("Enter 2D list data (example: [[1,2,3],[4,5]])")
L = eval(input())

print("Elements are:")
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end="\t")
    print()