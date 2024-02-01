x = int(input())
for i in range(x+1):
    line = "  " * (x-i)
    a=0
    for j in range((i*2)+1):
        if (j <= ((i*2)+1)//2): 
            line+= str(j) + " "
            a=j
        else: 
            a-=1
            line+= str(a) + " "
    print(line[:-1])

for i in range(x,0,-1):
    line= "  " * (x+1-i)
    a=0 
    for j in range((i-1)*2 + 1):
        if (j <= (((i-1)*2)+1)//2): 
            line+= str(j) + " "
            a=j
        else: 
            a-=1        
            line+= str(a) + " "
    print(line[:-1])

