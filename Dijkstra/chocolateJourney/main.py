import queue
MAX = 100
INF = int(1e9)

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist < other.dist
    
def Dijkstra(s):
    pq = queue.PriorityQueue()

    pq.put(Node(s,0))
    dist[s] = 0

    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u
        
if __name__ == '__main__':
    info = map(int, input().split())

    N,M,k,x = info

    chocoCity = map(int, input().split())

    graph = [[] for i in range(N + 1)]
    dist = [INF] * 100000
    path = [-1 for i in range(N + 1)]

    for i in range(M):
        d = map(int, input().split())
        a,b, weight = d
        graph[a].append(Node(b, weight))
        graph[b].append(Node(a, weight))

    findPath = map(int, input().split())
    st, en = findPath

    Dijkstra(st)

    minDist = INF
    choco = 0   

    for i in chocoCity:
        if minDist > dist[i]:
            minDist = dist[i]
            choco = i
    
    dist = [INF] * 100000
    path = [-1 for i in range(N + 1)]

    Dijkstra(choco)

    if dist[en] == INF:
        print(-1)
    else:
        if dist[en] > x:
            print(-1)
        else:
            print(dist[en]+ min)

    


        

