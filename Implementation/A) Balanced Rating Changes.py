flag = 1
for _ in range(int(input())):
    x = int(input())
    if x%2 == 0: print(x//2)
    else:
        print((x + flag)//2)
        flag *= -1
