MAX = 10000

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])

    return parent[u]

def union(u,v):
    pu = find(u)
    pv = find(v)

    if pu == pv: # This line is neccessary
        return 
    if ranks[pu] < ranks[pv]:
        parent[pu] = pv
        num[pv] += num[pu]
    elif ranks[pv] < ranks[pu]:
        parent[pv] = parent[pu]
        num[pu] += num[pv]
    else:
        parent[pv] = pu
        num[pu] += num[pv]
        ranks[pu] += 1

test = int(input())

for t in range(test):
    blank = input()
    m,n = map(int, input().split())
    parent = [i for i in range(m)]
    ranks = [0] * (m)
    num = [1] * (m)
    opinion_graph = [set() for _ in range(MAX)]


    while True:
        try:
            person, tree = map(int, input().split())
        except:
            break
        
        person -= 1
        tree -= 1

        opinion_graph[person].add(tree)

    for x in range(m):
        for y in range(x + 1, m):
            if opinion_graph[x] == opinion_graph[y]:
                union(x,y)
    for i in range(m):
        parent[i] = find(i)

    print(len(set(parent)))
    print()

    # Ask TA
    
        
    
     