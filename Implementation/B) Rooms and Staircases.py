for _ in range(int(input())):
    x = int(input())
    s = str(input())

    if s[0] == '1' or s[-1] == '1': print(x*2)
    else:
        l,r = -1, -1
        #checking from right side where stair is
        for i in range(x-1,-1,-1):
            if s[i]== '1':
                r = i+1
                # r is i + 1 because in array rooms are from 0 to x-1, but room number are from 1 to x
                break
        #checking from the left side fro stairs
        for i in range(x):
            if s[i]== '1':
                l = i+1
                break
        #print(l,r)
        if l!=-1:
            print(2*(x - min(l,r) + 1))
        else:
            print(x)
