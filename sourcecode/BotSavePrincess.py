#!/usr/bin/python
from tracemalloc import start
import queue

  

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())


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



nums = queue.Queue()
nums.put("")
add = ""


while not findPrincess(grid, add): 
    add = nums.get()
    
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if validation(grid, put):
            nums.put(put)
            