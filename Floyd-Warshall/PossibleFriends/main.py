def Floyd(dist, M):
    for k in range(M):
        for i in range(M):
            if dist[i][k] == INF:
                continue
            for j in range(M):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j] 


INF = 10 ** 9
T = int(input())

for _ in range(T):
    line = input()
    M = len(line)
    dist = [[INF] * M for _ in range(M)]
    for i in range(M):
        if i != 0:
            line = input()
        for j in range(M):
            if line[j] == 'Y':
                dist[i][j] = 1
    
    for i in range(M):
        dist[i][i] = 0
    
    Floyd(dist, M)

    maxCount = 0
    maxID = 0

    for i in range(M):
        count = 0
        for j in range(M):
            if dist[i][j] == 2:
                count += 1
        if count > maxCount:
            maxCount = count
            maxID = i

    print(maxID, maxCount) 