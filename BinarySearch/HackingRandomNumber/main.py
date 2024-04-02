def binarySearch(arr, indx,  x):
    if indx + 1 >= len(arr):
        return 0
    f1 = a[indx]
    l = indx + 1
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
    
        if mid >= len(arr):
            return 0
        if abs(a[mid] - f1) > x:
            r = mid - 1
        elif abs(a[mid] - f1) < x:
            l = mid + 1
        elif abs(a[mid] - f1)  == x:
            return 1
          
    return 0

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 0

binarySearch(a, 1, k)

for i in range(len(a)):
    cnt += binarySearch(a, i, k)


print(cnt)


