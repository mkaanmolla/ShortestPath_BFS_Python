#!/usr/bin/python
from tracemalloc import start
import queue



m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

#"validation" is a function for testing the move is valid or not.
#For example if your grid is like   -m-  bot could go upward however, it is invalid. 
#                                   ---
#                                   -p- 
def validation (grid, moves):
    for j in range(m):
        for x, pos in enumerate(grid[j]):
            if pos == "m":
                startcolumn=x
                startrow=j
    
    i=startcolumn
    j=startrow
    #print(f"J: {j} I: {i}")
    #print(len(grid))   
    for move in moves:
        if move == "L":
            i-=1
        elif move == "R":
            i +=1
        elif move == "U":
            j -=1
        elif move =="D":
            j +=1
        if not ((0<=i<len(grid)) and (0 <=j<len(grid))):
            return False
    return True

#"findPrincess" is a function for finding the princess.
# If our bot (m) go to the same position in our grid list it will return true and also prints the moves exactly.
def findPrincess (grid, moves):
    for j in range(m):
        for x, pos in enumerate(grid[j]):
            if pos == "m":
                startcolumn=x
                startrow=j
    
    i=startcolumn
    j=startrow
    for move in moves:
        if move == "L":
            i-=1
        elif move == "R":
            i +=1
        elif move =="U":
            j -=1
        elif move =="D":
            j +=1
    if grid[j][i]=="p":
        for move in moves:
            if move=="L":
                print("LEFT")
            elif move == "R":
                print("RIGHT")
            elif move == "U":
                print("UP")
            elif move == "D":
                print("DOWN")
        return True
    return False


#The following lines show the main algorithm. Queue is a default library in Python 3.
# put() --> puts an element to the queue
# get() --> gets an element from the queue
# Basic BFS algorithm is used in the following lines.
nums = queue.Queue()
nums.put("")
add = ""


while not findPrincess(grid, add): 
    add = nums.get()
    
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if validation(grid, put):
            nums.put(put)
            
