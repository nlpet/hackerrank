from sys import stdin

data = [[int(y) for y in x.strip().split(' ')]
                for x in stdin.readlines()]

sdata = set(data[1])
s = sum(sdata)
t = len(sdata)

print(s / t)
