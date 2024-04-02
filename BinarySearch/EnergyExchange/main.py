INF = 1e-8
n, k = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

l = a[0]
r = a[len(a) - 1]
sum = 0


for i in a:
    sum += i

while(l+INF<r):
    mid = (l + r) / 2
    sum2 = 0

    print(f"l: {l} | r: {r} | mid: {mid}")

    for i in a:
        if i > mid:
            sum2 += i - mid
    if (sum - n * mid) == (k) * sum2 / 100:
        print(f"{mid:.7f}")
        break
    if (sum - n * mid) > (k) * sum2 / 100:
        l = mid
    else:
        r = mid

print(f"{r:.7f}")
