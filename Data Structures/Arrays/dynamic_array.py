import sys
# n = number of sequences
# q = number of queries
n, q = [int(x) for x in input().strip().split(' ')]

seq_list = [[] for _ in range(n)]
last_ans = 0

for _ in range(q):
    qt, x, y = [int(x) for x in input().strip().split(' ')]
    indx = (x ^ last_ans) % n
    if qt == 1:
        seq_list[indx].append(y)
    elif qt == 2:
        last_ans = seq_list[indx][y % len(seq_list[indx])]
        print(last_ans)
    
