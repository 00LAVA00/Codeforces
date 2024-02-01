for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    new = [(a[i], b[i]) for i in range(n)]
    new.sort()
    for i in new:
        print(i[0], end=" ")
    print()
    for i in new:
        print(i[1], end=" ")
    print()
