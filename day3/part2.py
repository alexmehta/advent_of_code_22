summ = 0
while True:
    first,second,third= input(),input(),input()
    if(first=='end'):
        break
    intersection = list(set(first)&set(second)&set(third))
    for char in intersection:
        if(char.isupper()):
            summ += (ord(char) -64) + 26 
        else:
            summ += (ord(char) -96)
       
print(summ)
