#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    ix = n//2
    iy = n//2
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                fx = i
                fy = j
                
    if fx>ix:
        for k in range(fx-ix):
            print("DOWN")
    else:
        for k in range(ix-fx):
            print("UP")
    if fy>iy:
        for k in range(ix-fx):
            print("RIGHT")
    else:
        for k in range(iy-fy):
            print("LEFT")
                
                
#print all the moves here


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)