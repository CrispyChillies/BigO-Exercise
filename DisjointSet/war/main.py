parent = []
ranks = []

def makeSet(MAX):
    global parent, ranks, nums
    parent = [i for i in range(MAX * 2)]
    ranks = [0 for i in range(MAX  * 2)]
    nums = [1 for i in range(MAX * 2)]

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

if __name__ == "__main__":
    n = int(input())
    makeSet(n)
    
    while True:
        c, x, y = map(int, input().split())
        if c == 0 and x == 0 and y == 0:
            break
        if c == 1:
            if findSet(x) == findSet(y + n):
                print(-1)
            else:
                unionSet(x,y)
                unionSet(x + n, y + n)
        elif c == 2:
            if findSet(x) == findSet(y):
                print(-1)
            else:
                unionSet(x, y + n)
                unionSet(x + n, y)
        elif c == 3:
            if findSet(x) == findSet(y):
                print(1)
            else:
                print(0)
        elif c == 4:
            if findSet(x) == findSet(y + n):
                print(1)
            else:
                print(0)