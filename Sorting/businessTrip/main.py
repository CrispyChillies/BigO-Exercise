k = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

cnt = 0
for i in range(len(arr)):
    if k <= 0:
        break
    k -= arr[i]
    cnt += 1
if k <= 0:
    print(cnt)
else:
    print(-1)
