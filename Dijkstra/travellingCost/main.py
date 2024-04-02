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
    graph = [[] for i in range(501)]
    dist = [INF] * 501
    path = [-1 for i in range(501)]
    
    for i in range(n):
        d = map(int, input().strip().split())
        a,b, weight = d
        graph[a].append(Node(b, weight))
        graph[b].append(Node(a, weight))
    
    s = int(input())
    Dijkstra(s)

    q = int(input())

    for i in range(q):
        v = int(input())
        if dist[v] != INF:
            print(dist[v])
        else:
            print("NO PATH")
    
    
    
    



    

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
    graph = [[] for i in range(501)]
    dist = [INF] * 501
    path = [-1 for i in range(501)]
    
    for i in range(n):
        d = map(int, input().strip().split())
        a,b, weight = d
        graph[a].append(Node(b, weight))
        graph[b].append(Node(a, weight))
    
    s = int(input())
    Dijkstra(s)

    q = int(input())

    for i in range(q):
        v = int(input())
        if dist[v] != INF:
            print(dist[v])
        else:
            print("NO PATH")
    
    
    
    



    

