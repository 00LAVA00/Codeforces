for _ in range(int(input())):
    m, n = map(int, input().split())
    matrix= []
    count=0
    for i in range(m):
        arr= str(input())
        matrix.append(arr)
    count+=sum(j[-1]=='R' for j in matrix)
    count+=matrix[-1].count('D')
    print(count)
