
# average number of successes that occur in a specified region
lam1 = 0.88
lam2 = 1.55

def pd(lam):
    return lam + lam ** 2

c_a = 160 + 40 * pd(lam1)
c_b = 128 + 40 * pd(lam2)

print('{0:.3f}'.format(c_a))
print('{0:.3f}'.format(c_b))
