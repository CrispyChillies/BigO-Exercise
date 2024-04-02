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
    size = int(input())
    for i in range(size):
        info = map(int, input().split())

        n, m, k, s, t = info

        graph = [[] for i in range(100000)]
        
        for i in range(m):
            d = map(int, input().strip().split())
            a,b, weight = d
            graph[a].append(Node(b, weight))
        
        dist = [INF] * 100000
        path = [-1 for i in range(100000)]
        Dijkstra(s)
        d1 = dist[t]
        print(d1)
        
        for _ in range(k):
            d = map(int, input().strip().split())
            a, b, weight = d
            existing_edge = next((edge for edge in graph[a] if edge.id == b), None)
            if existing_edge is None or weight < existing_edge.dist:
                graph[a] = [edge for edge in graph[a] if edge.id != b]  # Remove old edge if it exists
                graph[a].append(Node(b, weight))  # Add new edge
                graph[b] = [edge for edge in graph[b] if edge.id != a]  # Remove old edge if it exists
                graph[b].append(Node(a, weight))  # Add new edge

        dist = [INF] * 100000
        path = [-1 for i in range(100000)]
        Dijkstra(s)
        d2 = dist[t]
        print(d2)

        if d1 != INF or d2 != INF:
            print(min(d1, d2))
        else:
            print(-1)
        
        
        
        



        

