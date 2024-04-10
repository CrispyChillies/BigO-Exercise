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

def addLocation(location, index):
    if location in dict:
        return dict, index
    dict[location] = index 
    return dict, index + 1
    

# dict["ahihi"] = 1

# if 1 in dict.values():
#     print(dict["ahihi"])
# else:
#     print("No")

T = int(input())
n = 100000
cnt = 1
for _ in range(T):
    dict = {}
    index = 0
    blank = input()

    m = int(input())    

    graph = [[] for i in range(n)]
    dist = [INF for i in range(n)]
    path = [-1 for i in range(n)]
    visited = [False for i in range(n)]

    for i in range(m):
        start,end ,w = map(str, input().split())
        weight = int(w)
        
        dict, index = addLocation(start, index)
        dict, index = addLocation(end, index)
        
        graph[dict[start]].append(Node(dict[end], weight))
        graph[dict[end]].append(Node(dict[start], weight))
    
    prims(0)

    totalCost = 0

    checkINF = False
    for i in range(len(dict)):
        if dist[i] == INF:
            checkINF = True
            break
        totalCost += dist[i]

    if checkINF:
        print(f"Case {cnt}: Impossible")
    else:
        print(f"Case {cnt}: {totalCost}")

    cnt += 1
    





