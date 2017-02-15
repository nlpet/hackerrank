N = int(input().strip())

# just one stack
queue = []

for _ in range(N):
    q = [int(x) for x in input().strip().split(' ')]
    if q[0] == 1:
        queue.append(q[1])
    elif q[0] == 2:
        del queue[0]
    else:
        print(queue[0])
