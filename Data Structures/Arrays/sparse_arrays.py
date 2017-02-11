'''
# Solution using a dict

from collections import defaultdict

d = defaultdict(int)
n = int(input().strip())

for _ in range(n):
    s = input().strip()
    d[s] += 1

q = int(input().strip())

for _ in range(q):
    s = input().strip()
    print(d.get(s, 0))
'''

# Solution using an array

n = int(input().strip())
arr = []

for _ in range(n):
    s = input().strip()
    arr.append(s)

q = int(input().strip())

for _ in range(q):
    s = input().strip()
    match = 0
    for i in range(len(arr)):
        if s == arr[i]:
            match += 1
    print(match)
    
