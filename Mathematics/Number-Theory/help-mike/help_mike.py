import sys
data = [[int(y) for y in x.strip().split(' ')] 
                for x in sys.stdin.readlines()]

def number_of_pairs(N, K):
  count = 0
  for i in range(1, K + 1):
    for j in range(i + 1, K + 1):
      if (i + j) % K == 0: count += 1
  return count
    
                
for N, K in data[1:]:
    sys.stdout.write(str(number_of_pairs(N, K))+'\n')
