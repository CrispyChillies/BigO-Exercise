def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])

    return parent[u]

def union(u,v):
    pu = find(u)
    pv = find(v)

    if pu == pv: 
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
    n,m = map(int, input().split())
    parent = [i for i in range(n)]
    ranks = [0] * n
    num = [1] * n

    for i in range(m):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        union(a,b)

    answer = 0
    for i in range(n):
        if i == parent[i] and num[i] > answer:
            answer = num[i]
    print(answer)