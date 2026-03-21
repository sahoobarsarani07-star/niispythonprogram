L1 = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(L1)):
    for j in range(len(L1[i])):
        if i == j:
            print(L1[i][j], end="\t")
        else:
            print("\t", end="")
    print()