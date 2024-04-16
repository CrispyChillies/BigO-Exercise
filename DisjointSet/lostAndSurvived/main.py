parent = []
ranks = []

def makeSet(MAX):
    global parent, ranks, nums
    parent = [i for i in range(MAX)]
    ranks = [0 for i in range(MAX)]
    nums = [1 for i in range(MAX)]

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
        nums[up] += nums[vp]
        nums[vp] = nums[up]
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        nums[vp] += nums[up]
        nums[up] = nums[vp]
    else:
        parent[up] = vp
        ranks[vp] += 1
        nums[vp] += nums[up]
        nums[up] = nums[vp]

n,q = map(int, input().split())


makeSet(n)
for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    
    unionSet(u,v)
    
    for i in range(n):
        parent[i] = findSet(i)

    numberOfGroup = len(set(parent))

    if numberOfGroup != 1:
        largest = max(nums)
        smallest = min(nums)
        print(largest - smallest)
    else:
        print(0)