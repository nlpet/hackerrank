
p = 1 / 3
n = 5


def g(n, p):
    return ((1 - p) ** (n - 1)) * p


print('{0:.3f}'.format(g(n, p)))
