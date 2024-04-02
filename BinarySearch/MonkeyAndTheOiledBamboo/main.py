def findK(heights):
    if len(heights) == 1:
        return heights[0]
    max = heights[0] - 0
    for i in range(1,len(heights)):
        if max < heights[i] - heights[i-1]:
            max = heights[i] - heights[i-1]

    return max

def checkClimb(heights, K):
    cnt = 0
    for i in range(1,len(heights)):
        if heights[i] - heights[i-1] == K:
            cnt += 1
    if cnt > K:
        return cnt - K
    else:
        return 0

T = int(input())

cnt = 1

for _ in range(T):
    rungs = int(input())
    heights = list(map(int, input().split()))
    result = findK(heights)
    result += checkClimb(heights, result)
    print(f"Case {cnt}: {result}")
    cnt += 1