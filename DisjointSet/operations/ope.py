MAX = 20
parent = []
ranks = []

def makeSet():
    global parent, ranks
    parent = [i for i in range(MAX + 5)]
    ranks = [0 for i in range(MAX + 5)]
    nums = [1 for i in range(MAX + 5)]

def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u,v):
    up = findSet(u)
    vp = findSet(v)

    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1

    
if __name__ == '__main__':
    Q = int(input())
    makeSet()
    for i in range(Q):
        u,v,q = map(int, input().split())
        if q == 1:
            unionSet(u,v)
        if q == 2:
            parentU = findSet(u)
            parentV = findSet(v)
            if parentU == parentV:
                print("Yes")
            else:
                print("No")
