
input = open("input01.txt").readlines()
output = open("output01.txt").readlines()

for i in range(len(input)):
	N,C,M = map(int,input[i].split())

	answer = N / C
	wrappers = answer

	while M <= wrappers:
		answer += wrappers / M
		wrappers -= M
		wrappers += wrappers % M

	if answer != int(output[i]):
		print answer, int(output[i]), (N,C,M)

	
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    N,C,M = [int(x) for x in raw_input().split(' ')]
    if C > N:
        print 0
        continue
    answer = N // C
    wrappers = answer

    while M <= wrappers:
        answer += wrappers // M
        wrappers -= M
        wrappers += wrappers % M
    
    print int(answer)

'''