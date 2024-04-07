n = int(input())
arr = list(map(int, input().split()))
di = {arr[i]:i for i in range(n)}
arr = sorted(arr)
m = 1e17
for i in range(1,n):
    if di[arr[i]] < di[arr[i-1]]:
        m = min(m, arr[i] - arr[i-1])
print(m)