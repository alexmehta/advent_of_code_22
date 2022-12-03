def determine_move(opp,ans):
    #lose
    if(ans=='X'):
        if(opp=='A'):
            return 'Z'
        if(opp=='B'):
            return 'X'
        if(opp=='C'):
            return 'Y'
    #tie
    if(ans=='Y'):
        if(opp=='A'):
            return 'X'
        if(opp=='B'):
            return 'Y'
        if(opp=='C'):
            return 'Z'
    #win
    if(ans=='Z'):
        if(opp=='A'):
            return 'Y'
        if(opp=='B'):
            return 'Z'
        if(opp=='C'):
            return 'X'
def get_score(opp,you):
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
    return score       
total = 0
while True:
    s = input()
    if(s == "end"):
            break
    s = s.split()
    opp = s[0]
    you = s[1]
        
    total += get_score(opp,determine_move(opp,you))
print(total)

