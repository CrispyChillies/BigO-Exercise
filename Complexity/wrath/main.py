n = int(input())
a = list(map(int, input().split()))

prev = 0
alive = n

for i in range(len(a) - 1, -1, -1):
    prev = i - 1
    if prev == -1:
        break
    if i > prev and prev >= i - a[i]:
        alive -= 1
        a[prev] = a[i]

print(alive)