import operator
if __name__ == "__main__":
    elfs = [0]
    elf = 0
    while True:
        num = input()
        if(num ==""):
            elf+=1
            elfs.append(0)
            continue
        if(num=="end"):
            break
        elfs[elf]+= int(num)
    value = sorted(elfs)
    print(sum(value[-3:]))
