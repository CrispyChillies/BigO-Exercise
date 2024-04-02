def findMin(heights, q):
    if q > max(heights):
        return max(heights)
    result = 0
    for i in range(len(heights)):
        if heights[i] > q or heights[i] == q:
            result = i - 1
            break
    if result >= 0:
        return heights[result]
    else:
        return "X"

def findMax(heights, q):
    if q < heights[0]:
        return heights[0]
    result = -1
    for i in range(len(heights)):
        if heights[i] > q:
            result = i
            break
    if result >= 0:
        return heights[result]
    else:
        return "X"

N = int(input())

heights = list(map(int, input().split()))

Q = int(input())

queries = list(map(int, input().split()))

for query in queries:
    print(f"{findMin(heights, query)} {findMax(heights, query)}") 






