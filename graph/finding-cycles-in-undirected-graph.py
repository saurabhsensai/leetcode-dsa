adj = [[], [2], [1, 3], [2]] 

def detect(src, adj, visited):
    visited.append(src)
    q = []
    q.append((src, -1))
    
    while q:
        node = q[0][0]
        previous = q[0][1]
        q.pop(0)
        
        for i in adj[node]:
            if i not in visited:
                visited.append(i)
                q.append((i, node))
            elif previous != i:
                return True
    
    return False

visited = []
for i in range(len(adj)):
    if i not in visited:
        if (detect(i , adj , visited)) == True:
            print("True")
    
