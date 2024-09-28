image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0


def bfs(sr, sc, color, image):
    visited = []
    queue = []
    n = len(image)
    m = len(image[0])
    orignal = image[sr][sc]
    visited.append((sr, sc))
    queue.append((sr, sc))
    
    while queue:
        sr, sc = queue[0][0], queue[0][1]
        queue.pop(0)
        image[sr][sc] = color
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for dr, dc in directions:
            nrow , ncol = sr + dr , sc + dc 
            if (nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and image[nrow][ncol] == orignal and (nrow, ncol) not in visited):
                queue.append((nrow, ncol))
                visited.append((nrow, ncol))
                
bfs(sr, sc, color, image)
print(image)        
        

