import queue
from math import sqrt

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
    
    while True:
        try:
            n = int(input())
        except:
            break

        coordinate = []
        graph = [[] for i in range(n)]
        dist = [INF for i in range(n)]
        path = [-1 for i in range(n)]
        visited = [False for i in range(n)]

        for _ in range(n):
            x, y = map(int, input().split())
            coordinate.append([x, y])

        m = int(input())
        subtractDist = 0

        for _ in range(m):
            start, end = map(int, input().split())
            start -= 1
            end -= 1
            #    visited[start] = True
            #    visited[end]  = True
            #    path[end] = start 
            #    dist[start] = 0
            w = 0 #sqrt((coordinate[start][0] - coordinate[end][0]) ** 2 + (coordinate[start][1] - coordinate[end][1]) ** 2)
            graph[start].append(Node(end, w))
            graph[end].append(Node(start, w))

        for i in range(n):
            for j in range(i + 1, n):
                # print(len(coordinate))
                # print(f"{i} - {j}")
                w = sqrt((coordinate[i][0] - coordinate[j][0]) ** 2 + (coordinate[i][1] - coordinate[j][1]) ** 2)

                graph[i].append(Node(j, w))
                graph[j].append(Node(i, w))
        prims(0)

        totalCost = 0

        for d in dist:
            totalCost += d
        print(f"total cost : {totalCost} - substract: {subtractDist}")
        print(f"{(totalCost):.2f}")

