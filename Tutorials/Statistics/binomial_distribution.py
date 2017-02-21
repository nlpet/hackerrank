# Task
#
# The ratio of boys to girls for babies born in Russia is 1.09: 1.
# If there is 1 child born per birth, what proportion of Russian families with exactly 6
# children will have at least 3 boys?
from math import factorial as fac

p = 1.09 / 2.09
q = 1 - p


def binomial(x, n, p):
    return (fac(n) / (fac(x) * fac(n - x))) * (p ** x) * (q ** (n - x))

at_least_three_boys = 0

for x in range(3, 7):
    at_least_three_boys += binomial(x, 6, p)

print('{0:.3f}'.format(at_least_three_boys))
