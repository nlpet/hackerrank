



n,m = 4, 3
a = [1, 2, 3, 4]
b = [1, 2, 3]
c = [13, 29, 71]



mod = 10**9+7


'''
n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
c = map(int, raw_input().split())
'''

mas = [1]*(n+1)
for ind in xrange(m):
    mas[b[ind]] = mas[b[ind]] * c[ind] % mod

for step in xrange(1, n+1):
    for a_ind in xrange(step-1, n, step):
        a[a_ind] = a[a_ind]*mas[step] % mod

print ' '.join(map(str, a))
