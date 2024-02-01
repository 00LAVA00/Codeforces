count=0
for _ in range(int(input())):
    s= str(input())
    if '+' in s: count+=1
    elif '-' in s: count-=1
    else: continue
print(count)