n = int(input())
a = list(map(int, input().split()))

right = 0
best = 0
count = 0

fre = 100001 * [0]

for left in range(n):
    while right < n and count <= 2:
        if count == 2 and fre[a[right]] == 0:
            break
        if fre[a[right]] == 0:
            count += 1
        fre[a[right]] += 1
        right += 1
        
    best = max(best, right - left)

    if fre[a[left]] == 1:
        count -= 1
    fre[a[left]] -= 1
    if right == n - 1:
        break
print(best)