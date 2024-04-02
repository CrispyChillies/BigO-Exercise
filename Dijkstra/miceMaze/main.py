import queue
MAX = 100
INF = int(1e9)

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist
    
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
    n = int(input())
    out = int(input())
    timeout = int(input())

    graph = [[] for i in range(n + 5)]
    
    path = [-1 for i in range(n + 5)]

    connection = int(input())
    
    for i in range(connection):
        d = map(int, input().strip().split())
        a,b, weight = d
        graph[a].append(Node(b, weight))
    
    cnt = 0
    for i in range(1, n + 1):
        dist = [INF] * 501
        Dijkstra(i)
        if dist[out] <= timeout:
            cnt += 1
    
    print(cnt)


    
    
    
    



    

