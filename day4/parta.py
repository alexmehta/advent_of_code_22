def process(a,b):
    return int(a.split("-")[0]),int(a.split("-")[1]),int(b.split("-")[0]),int(b.split("-")[1])

ans = 0

t = 0
while True:

    print(ans)
    elf = input()
    counts = dict()
    if(elf=='end'):
        break
    a,b  = elf.split(',')
    print(a,b)
    a,b,c,d  = process(a,b)
    for i in range(a,b+1):
        if(i not in counts):
            counts[i]= 1
        else:
            counts[i]+=1  
    for i in range(c,d+1):
        if(i not in counts):
            counts[i]=1
        else:
            counts[i]+=1
    for i in range(a,b+1):
        if(counts[i]!=2):
            break 
    else:
        ans+=1
        continue
    for i in range(c,d+1):
        if(counts[i]!=2):
            break 
    else:
        ans+=1
        continue 
print(ans)
