n = int(input())

arr = list(map(int, input().split()))

arr.sort()

if len(arr) % 2 == 0:
    f1 = len(arr) / 2
    f2 = f1 - 1
    print((arr[f1] + arr[f2]) / 2 )
else:
    print(arr[round(len(arr) / 2 - 0.5)])

