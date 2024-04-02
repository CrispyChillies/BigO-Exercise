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
    N = int(input())

    cnt = 1
    for i in range(N):

        info = map(int, input().split())

        n, m, S, T = info

        graph = [[] for i in range(n + 1)]
        dist = [INF] * 100000
        path = [-1 for i in range(n + 1)]
        
        for i in range(m):
            d = map(int, input().strip().split())
            a,b, weight = d
            graph[a].append(Node(b, weight))
            graph[b].append(Node(a, weight))
        
        Dijkstra(S)

        if dist[T] == INF or m == 0:
            print(f"Case #{cnt}: unreachable")
        else:
            print(f"Case #{cnt}: {dist[T]}")
        cnt += 1
        



        

