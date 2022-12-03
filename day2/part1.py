if __name__ == "__main__":
    total = 0
    while True:
        s = input()
        if(s == "end"):
            break
        s = s.split()
        opp = s[0]
        you = s[1]
        score = 0
        if(opp=="A"):
            if(you=="X"):
                score += 3
            elif(you=="Y"):
                score += 6
            elif(you=="Z"):
                score += 0
        elif(opp=="B"):
            if(you=="X"):
                score +=0 
            elif(you=="Y"):
                score +=3 
            elif(you=="Z"):
                score += 6
        elif(opp=="C"):
            if(you=="X"):
               score +=6 
            elif(you=="Y"):
               score += 0
            elif(you=="Z"):
               score += 3
        if(you=='X'):
            score += 1
        elif(you=='Y'):
            score+=2
        elif(you=='Z'):
            score+=3

        total += score
       # print(opp,you,score) 
    print(total)
