import math
import time

'''
N, M = map(int, raw_input().split())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
C = map(int, raw_input().split())
'''

start_time = time.time() # start marking time

N, M = 4, 3
A = [1, 2, 3, 4]
B = [1, 2, 3]
C = [13, 29, 71]


for i in xrange(1, M + 1):
	for j in xrange(1, N + 1):
		if j % B[i - 1] == 0:
			A[j - 1] *= C[i - 1]

print ' '.join([str(n % 1000000007) for n in A])

elapsed_time = time.time() - start_time
print("Elapsed time",elapsed_time*1000000000,"nanosecond")


start_time = time.time() # start marking time

N, M = 4, 3
A = [1, 2, 3, 4]
B = [1, 2, 3]
C = [13, 29, 71]

for i in xrange(1, M + 1):
	for j in xrange(B[i-1], N + 1):
		if j % B[i - 1] == 0:
			A[j - 1] *= C[i - 1]

print ' '.join([str(n % 1000000007) for n in A])

elapsed_time = time.time() - start_time
print("Elapsed time",elapsed_time*1000000000,"nanosecond")

'''
for i1 in xrange(1, M + 1):
	#all numbers that divide B[i-1], range >= B[i-1] <=  N
	pass


print ' '.join([str(n % 1000000007) for n in A])
'''