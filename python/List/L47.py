L1 = [[1,2,3],[4,5,6]]
L2 = [[3,4,1],[2,2,4]]
L3 = []

for i in range(len(L1)):
    row = []
    for j in range(len(L1[i])):
        row.append(L1[i][j] + L2[i][j])
    L3.append(row)
print(L3)