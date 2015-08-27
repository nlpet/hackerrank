
n = map(int, raw_input().split())[0]
ss = []

for _ in range(n):
	ss.append(set(raw_input().split()[0]))

print len(set.intersection(*ss))
