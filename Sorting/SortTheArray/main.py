n = int(input())
arr = list(map(int, input().split()))

sortArr = arr.copy()
sortArr.sort()

diff = 0
ans = []    

ans.append(arr[0])

for i in range(len(arr)):
    if arr[i] != sortArr[i]:
        diff += 1
        ans.append(arr[i])

if diff == 2:
    print("yes")
    print(ans[2], ans[1])
elif diff == 0:
    print("yes")
    print(ans[0], ans[0])
else:
    print("no")