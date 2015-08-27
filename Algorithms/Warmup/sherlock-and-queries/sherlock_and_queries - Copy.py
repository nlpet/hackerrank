import sys

'''
N, M = map(int, raw_input().split())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
C = map(int, raw_input().split())
'''

def divs(num):
    ld = []
    for i in xrange(1, int(math.sqrt(num) + 1)):
        if num % i is 0:
            yield i
            if i is not num / i:
                ld.insert(0, num / i)
    for divisor in ld:
        yield divisor


N, M = 4, 3
A = [1,2,3,4]
B = [6,3,2]
C = [13,29,71]


for i in xrange( 1, M + 1):
	for j in xrange( 1, N + 1):
		if j % B[i-1] == 0: A[j-1] = A[j-1] * C[i-1]

print ' '.join([str(n%(1000000007)) for n in A])


divisors = []

for j in xrange(1, N+1):
	divisors.append(list(divs(j)))
	

for i in xrange(1, M+1):
	if B[i-1] in divisors[i-1]: 
		A[divisors[i-1][B[i-1]]] = A[A.index(divisors[i-1][B[i-1]])] * C[i-1]
		
if B[i-1] in divisors then
	A[j-1]
	
j is the jth position in divisors and the divisor in jth pos is B[i-1]



for i in xrange(1, M+1):
	for num in 