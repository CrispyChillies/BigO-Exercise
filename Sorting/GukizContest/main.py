n = int(input())
originArr = list(map(int, input().split()))

arr = originArr.copy()
arr.sort(reverse=True)

rank = 1
downrank = 1
result = [0 for _ in range(2 * n)]

result = {}
result[arr[0]] = rank

for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        result[arr[i]] = rank
        downrank += 1
    if arr[i] != arr[i-1]:
        rank += downrank
        result[arr[i]] = rank
        downrank = 1

for i in originArr:
    print(result[i], end=' ')
    



