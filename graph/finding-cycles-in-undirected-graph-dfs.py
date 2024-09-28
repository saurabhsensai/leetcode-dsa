adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] 


def dfs(node, parent, visited, adj):
    visited.append(node)
    
    for i in adj[node]:
        if i not in visited:
            if (dfs(i , node , visited , adj)) == True:
                return True
        elif i != parent:
            return True
    return False
visited = []    
for i in range(len(adj)):
    if i not in visited:
        if (dfs(i, -1, visited, adj)) == True:
            print("True")
        else:
            print("False")

            
    
    
