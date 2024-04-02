import queue 

class Job:
    def __init__(self, id, prior) -> None:
        self.id = id
        self.prior = prior

test = int(input())

# max
for i in range(test):
    pq = queue.Queue()

    n,m = map(int, input().split())

    id_prior = list(map(int, input().split()))

    for j, prior in enumerate(id_prior):
        pq.put(Job(j, prior))

    cnt = 0
    
    while not pq.empty():
        task = pq.get()

        if any(task.prior < q.prior for q in pq.queue):
            pq.put(task)
        else:
            cnt += 1
            if task.id == m:
                print(cnt)
        




