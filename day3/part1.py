
summ = 0
while True:
    line = input()
    if(line=='end'):
        break
    first,second= line[:len(line)//2], line[len(line)//2:]
    print(first,second)
    intersection = list(set(first)&set(second))
    for char in intersection:
        print(char)
        if(char.isupper()):
            print((ord(char) -64)+26 ) 
            summ += (ord(char) -64) + 26 
        else:
            summ += (ord(char) -96)

            print((ord(char) -96) )
        print(summ)
print(summ)
