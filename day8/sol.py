import numpy as np
grid = [list(map(int, line)) for line in open('day8/acutal.txt').read().splitlines()]
grid = np.array(grid)
score = 0


for i in range(len(grid)):
    for j in range(len(grid[i])):
        k = grid[i][j]
        # this should go through all the trees in that col 
        if all(grid[i][z] < k for z in range(j)):
            score+=1
        #go check all to the left
        elif all(grid[i][z] < k for z in range(j + 1, len(grid[i]))):
            score+=1
        # check all "down"
        elif all(grid[z][j] < k for z in range(i)):
            score+=1
        #check all "up"
        elif all(grid[z][j] < k for z in range(i + 1, len(grid))):
            score += 1

print(score)
score = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        k = grid[i][j]
        L ,R, T , B = 0,0,0,0
        for x in range(j - 1, -1, -1):
            L += 1
            if grid[i][x] >= k:
                break
        for x in range(j + 1, len(grid[i])):
            R += 1
            if grid[i][x] >= k:
                break
        for x in range(i - 1, -1, -1):
            T += 1
            if grid[x][j] >= k:
                break
        for x in range(i + 1, len(grid)):
            B += 1
            if grid[x][j] >= k:
                break
        score = max(score, L * T * R *B)

print(score)
