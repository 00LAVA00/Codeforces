import copy
m, n = map(int,input().split())
oriMat = []
for i in range(m):
    row = list(map(int, input().split()))
    oriMat.append(row)
#print("o", oriMat)
count = 0
mat = copy.deepcopy(oriMat)

# if we got a zero while traversing the matrix we will make that columns and rows all entry zero. 
for i in range(m):
    for j in range(n):
        if (oriMat[i][j] == 0):
            for k in range(n): mat[i][k] = 0
            for h in range(m): mat[h][j] = 0
flag = False
for i in range(m):
    for j in range(n):
        y=0
        for k in range(n): y |= mat[i][k]
        for h in range(m): y |= mat[h][j]
        
        if y != oriMat[i][j]:
            print("NO")
            exit(0)



print("YES")

for i in range(m):
        print(*mat[i])
"""
for i in range(m):
    a =""
    for j in range(n):
        a+= str(mat[i][j]) + " "    
    print(a[:-1])


"""