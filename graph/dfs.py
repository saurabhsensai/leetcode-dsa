#Depth first search 

def dfss(node, adj, visited, dfs):
    visited.append(node)
    dfs.append(node)
    for i in adj[node]:
        if i not in visited:
            dfss(i, adj, visited, dfs)




visited = []
start = 0
dfs = []
adj = [[1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]]
    
dfss(start, adj, visited, dfs)    
print(dfs)
            
    
