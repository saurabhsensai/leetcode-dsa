grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def BFS(row, col, visited, grid):
    visited.append((row, col))
    queue = []
    queue.append((row, col))
    n = len(grid) #gives us row numbers
    m = len(grid[0])
    #code
    while(len(queue)):
        row = queue[0][0]
        col = queue[0][1]
        queue.pop(0)
        print((row, col))
        #traverse in neighbors
        for deltarow in range(-1, 2):
            for deltacol in range(-1, 2):
                if (deltarow, deltacol) not in () 
                nrow = row + deltarow
                ncol = col + deltacol
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == "1" and (nrow, ncol) not in visited:
                    print()
                    print((nrow, ncol))
                    visited.append((nrow, ncol))
                    queue.append((nrow, ncol))




n = len(grid) #gives us row numbers
m = len(grid[0]) #gives us column numbers
visited = []
count = 0
for row in range(n):
    for col in range(m):
        if (row,col) not in visited and grid[row][col] == "1":
            count += 1
            BFS(row,col,visited,grid)

print(count)       
            
