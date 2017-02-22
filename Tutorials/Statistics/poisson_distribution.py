from math import e, factorial

# actual number of successes that occur in a specified region
k = 5
# average number of successes that occur in a specified region
lam = 2.5

def p(k, lam):
    return (lam ** k * e ** -lam) / factorial(k)


print('{0:.3f}'.format(p(k, lam)))
