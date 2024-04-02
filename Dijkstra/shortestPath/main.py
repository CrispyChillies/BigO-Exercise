import queue
MAX = 100
INF = int(1e9)

class City:
    def __init__(self, name, id):
        self.name = name
        self.id = id

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
    test = int(input())
    cnt = 0
    for i in range(test):
        if cnt != 0:
            empty = input()
        cities = int(input())

        graph = [[] for i in range(100000)]
        city_map = {}
        id = 1
        for i in range(cities):
            name = input()
            city = City(name, id)
            id += 1

            city_map[city.name] = city.id

            neighbors = int(input())
            for j in range(neighbors):
                d = map(int, input().split())
                b, weight = d
                graph[city.id].append(Node(b, weight))

        findPath = int(input())
        
        for i in range(findPath):
            dist = [INF] * 100000
            path = [-1 for i in range(cities + 1)]
            name1, name2 = map(str, input().split())
            
            st = city_map[name1]
            en = city_map[name2]

            Dijkstra(st)
            print(dist[en])
        cnt += 1
        
        
        
        
        



        

