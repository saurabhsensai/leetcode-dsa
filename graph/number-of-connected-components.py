

isConnected = [[1,1,0],[1,1,0],[0,0,1]]

def DFS(node, adj, visited):
    visited.append(node)
    for i in adj[node]:
        if i not in visited:
            DFS(i, adj, visited)



adj = [[] for _ in range(len(isConnected))]

for i in range(0, len(isConnected)):
    for j in range(0, len(isConnected)):
        if isConnected[i][j] == 1 and i != j:
            adj[i].append(j)

visited = []
count = 0
for i in range(len(isConnected)):
    if i not in visited:
        count += 1
        DFS(i , adj , visited)
print(count)