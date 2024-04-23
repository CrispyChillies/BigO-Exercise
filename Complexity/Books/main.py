books, minutes = map(int, input().split())
timeToRead = list(map(int, input().split()))

cnt = 0
sum = 0
k = 0

for i in range(len(timeToRead)):
    sum += timeToRead[i]
    if sum < minutes:
        cnt += 1
    else:
        sum -= timeToRead[k]
        k += 1

print(cnt)