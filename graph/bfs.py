def BFS(adj):
    
    visited = []
    visited.append(0) #starting Node 
    bfs = []
    queue = []
    queue.append(0)
    
    while(len(queue)):
        node = queue[0]
        queue.pop(0)
        bfs.append(node)
        
        for i in adj[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
            
    return bfs
                

adj =  [[1,2], [0, 3,4], [0, 5,6], [1], [1], [2], [2]]      

print(BFS(adj))

