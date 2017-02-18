N = int(input().strip())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))

sum_weights = 0
weighed_sum = 0

for i in range(N):
    sum_weights += W[i]
    weighed_sum += X[i] * W[i]

print('{0:0.1f}'.format(weighed_sum / sum_weights))
