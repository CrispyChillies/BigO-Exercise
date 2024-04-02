n,m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

e = 0

for i in b:
    if i in a:  
        a.remove(i)
    for j in range(a):
        if a[j] > i:
            break
        else:
            a.remove(a[j])

print(len(a))
