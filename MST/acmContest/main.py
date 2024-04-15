import queue

INF = 1e9

class Node:
    def __init__(self, id, dist) -> None:
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist
    
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
        n, m = map(int, input().split())

        graph = [[] for i in range(n)]
        dist = [INF for i in range(n)]
        path = [-1 for i in range(n)]
        visited = [False for i in range(n)]

        for i in range(m):
            u,v,w = map(int, input().split())
            u -= 1
            v -= 1
            graph[u].append(Node(v, w))
            graph[v].append(Node(u, w))

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                print(f"Edge {i + 1}: {graph[i][j].id + 1} - {graph[i][j].dist}")
        
        prims(0)

        firstChoice = 0
        secondChoice = 0

        for cost in dist:
            firstChoice += cost

        sortDist = dist[:]
        sortDist.sort(reverse=True)
        print(sortDist)

        d = sortDist[0]
        print(d)
        print(f"dist = {dist}")

        #for d in dist:
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if d == graph[i][j].dist:
                    # print(f"{i + 1}, {graph[i][j].id + 1} - path = {d}")
                    graph[i][j].dist = INF 
                    print(graph[i][j].dist)

        print("List after changing")

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                print(f"Edge {i + 1}: {graph[i][j].id + 1} - {graph[i][j].dist}")
        prims(0)

        print(f"dist = {dist}")
            

        
        



