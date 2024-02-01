for _ in range(int(input())):
    x = int(input())
    print(2)
    a=x
    b=x-1
    for i in range(x-1):
        print(a,b)
        a = (a+b+1)//2
        b -= 1


#[if we take do a+b/2 from 1 to n the number increases, but if we do it from reverse it always comes 2]