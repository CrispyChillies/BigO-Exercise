import bisect

def bsFirst(a, x):
    pos = bisect.bisect_left(a, x)
    if pos >= len(a):
        return -1
    if a[pos] == x:
        return pos
    else:
        return -1

# def bsFirst(a,left, right, x):
#     if left <= right:
#         mid = (left + right) // 2
#         if mid >= n:
#             return -1
#         if (mid == left or x > a[mid-1]) and a[mid] == x:
#             return mid
#         elif x > a[mid]:
#             return bsFirst(a, mid + 1, right, x)
#         else:
#             return bsFirst(a, left, mid-1, x)
#     return -1

cnt = 1

while(True):
    n, q = map(int, input().split())
    if n  == 0 and q == 0:
        break
    arr = []
    for _ in range(n):
        numb = int(input())
        arr.append(numb)
    arr.sort()
    print(f"CASE# {cnt}:")
    for _ in range(q):
        Q = int(input())
        
        pos = bsFirst(arr, Q)
        if pos == -1:
            print(f"{Q} not found")
        else:
            print(f"{Q} found at {pos + 1}")
    cnt += 1