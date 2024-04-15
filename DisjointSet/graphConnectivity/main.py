parent = []
ranks = []
nums = []

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
        nums[vp] += nums[up]
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        nums[up] += nums[vp]
    else:
        parent[up] = vp
        ranks[vp] += 1
        nums[up] += nums[vp]


if __name__ == '__main__':
    T = int(input())
    blank = input()
    for _ in range(T):
        bigChar = input()
        rangeInput = ord(bigChar) - ord('A') + 1
        ans = rangeInput
        makeSet(rangeInput)

        while True:
            try:
                string = input().strip()
                if string == "":
                    break
                firstChar = ord(string[0]) - ord('A')
                secondChar = ord(string[1]) - ord('A')
                
                if findSet(firstChar) != findSet(secondChar):
                    unionSet(firstChar, secondChar)
                    ans -= 1

            except EOFError:
                break
        print(ans)
        print()
    


        
