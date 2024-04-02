INF = 10**9
MAX = 100000

class Edge:
    def __init__(self, src, des, weight):
        self.src = src
        self.des = des
        self.weight = weight

def BellmanFord(s):
    dist[s] = 0
    for i in range(1,n):
        for j in range(m):
            u = graph[j].src
            v = graph[j].des
            w = graph[j].weight

            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                path[v] = u
    
    # Check whether there is a negative circle inside the graph 
    for i in range(m):
        u = graph[i].src
        v = graph[i].des
        w = graph[i].weight

        if (dist[u] != INF) and (dist[u] + w < dist[v]):
            return False
    
    return True


c = int(input())

for i in range(c):
    dist = [INF for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]

    n,m = map(int, input().split())

    graph = [] 

    for i in range(m):
        u,v,w = map(int, input().split())
        graph.append(Edge(u,v,w))
    s = 0    
    if(BellmanFord(s)):
        print("not possible")
    else:
        print("possible")
    
