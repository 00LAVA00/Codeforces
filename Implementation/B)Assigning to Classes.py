for _ in range(int(input())):
    x = int(input())
    arr= list(map(int,input().split()))
    new_arr= sorted(arr)
    #print('n',new_arr)
    print(abs(new_arr[x]-new_arr[x-1]))