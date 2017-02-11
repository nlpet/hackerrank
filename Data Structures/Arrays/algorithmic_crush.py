n, m = [int(x) for x in input().strip().split(' ')]
arr = [0 for _ in range(n)]

max_value = 0
current_sum = 0

# use a prefix sum
for _ in range(m):
    a, b, k = [int(x) for x in input().strip().split(' ')]
    arr[a - 1] += k
    if b < n:
        arr[b] -= k

for el in arr:
    current_sum += el
    if current_sum > max_value:
        max_value = current_sum

print(max_value)
