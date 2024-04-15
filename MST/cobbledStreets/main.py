import queue

INF = 1e9

class Node:
    def __init__(self, id, dist) -> None:
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist
    
def printMST():
    ans = 0
    for i in range(n):  
        if path[i] == -1:
            continue
        ans += dist[i]
        print("{0} - {1}: {2}".format(path[i], i, dist[i]))
    print("Weight of MST: {0}".format(ans))

def prims(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v,w))
                path[v] = u

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        p = int(input())
        n = int(input())
        m = int(input())

        graph = [[] for i in range(n)]
        dist = [INF for i in range(n)]
        path = [-1 for i in range(n)]
        visited = [False for i in range(n)]

        for i in range(m):
            u,v,w = map(int, input().split())
            graph[u - 1].append(Node(v - 1, w))
            graph[v - 1].append(Node(u - 1, w))
        
        prims(0)

        totalCost = 0

        for d in dist:
            totalCost += d
        print(totalCost * p)

