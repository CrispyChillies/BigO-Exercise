import queue

INF = 10**9
MAX = 100000

class Edge:
    def __init__(self, src, des, weight):
        self.src = src
        self.des = des
        self.weight = weight

def BFS(s, graph):
    q = queue.Queue()
    visited[s] = True

    q.put(s)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)


def BellmanFord(s):
    dist[s] = 0
    for i in range(1, n):
        for j in range(m):
            u = graph[j].src
            v = graph[j].des
            w = graph[j].weight

            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u

    adjList = [[] for _ in range(MAX)]  
    for i in range(m):
        u = graph[i].src
        v = graph[i].des
        adjList[u].append(v)

    # Check whether there is a negative cycle inside the graph 
    for i in range(m):
        u = graph[i].src
        v = graph[i].des
        w = graph[i].weight
        
        if dist[u] != INF and dist[u] + w < dist[v]:
            # This vertex is part of the negative cycle
            BFS(u, adjList)
      

T = int(input())
cnt = 1

for _ in range(T):
    visited = [False] * MAX
    blank = input()

    n = int(input())
    busy = list(map(int, input().split()))

    m = int(input())

    dist = [INF for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]

    graph = [] 

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        t = (busy[v] - busy[u])
        w = t**3
        graph.append(Edge(u, v, w))
        
    q = int(input())
    
    print(f"Case {cnt}:")
    run = BellmanFord(0)

    for i in range(q):
        c = int(input()) - 1
        if visited[c]:
            print("?")
        else:
            if dist[c] == INF:
                print("?")
            elif dist[c] >= 3:
                print(dist[c])
            else:
                print("?")
    cnt += 1
