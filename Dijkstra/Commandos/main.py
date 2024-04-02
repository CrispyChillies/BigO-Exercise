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
    T = int(input())

    cnt = 1
    for i in range(T):

        N = int(input())
        R = int(input())

        graph = [[] for i in range(N + 1)]
        
        for i in range(R):
            d = map(int, input().strip().split())
            a,b = d
            graph[a].append(Node(b, 1))
            graph[b].append(Node(a, 1))
        
        st, en = map(int, input().split())
        
        dist = [INF] * 100000
        path = [-1 for i in range(N + 1)]
        
        Dijkstra(st)
        d1 = dist

        dist = [INF] * 100000
        path = [-1 for i in range(N + 1)]
        
        Dijkstra(en)
        d2 = dist
        
        mx = 0

        for i in range(N):
            mx = max(mx ,d1[i] + d2[i])
        
        print(f"Case {cnt}: {mx}")
        cnt += 1
        



        

