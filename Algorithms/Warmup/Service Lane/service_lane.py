import sys

s = sys.stdin.readlines()
data = []

for row in s:
    data.append([int(x) for x in row.split()])

width = data[1]
test_cases = data[2:]
	
for test in test_cases:
	print min(width[test[0]:test[1]+1]) 