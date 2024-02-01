num = int(input())
s = str(input())
for i in range(len(s)-1):
    if s[i] != s[i+1]: 
        print("YES")
        print(s[i]+s[i+1])
        exit(0)
print("NO")

#the string of two distinct letter is already diverse, so check for two consecutive different letters 