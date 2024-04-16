
def dfs(node):
    visited[node] = True
    for child in graph[node]:
        if visited[child] == False:
            dfs(child)
    

n,m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

dfs(0)
flag = 0

for i in range(n):
    if visited[i] == False:
        flag = 1

if n != m:
    flag = 1
    
if flag:
    print("NO")
else:
    print("FHTAGN!")