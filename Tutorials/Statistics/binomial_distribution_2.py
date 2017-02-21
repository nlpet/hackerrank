# Task
#
# A manufacturer of metal pistons finds that, on average, 12% of the pistons they
# manufacture are rejected because they are incorrectly sized. What is the probability
# that a batch of 10 pistons will contain:
#
# 1. No more than 2 rejects?
# 2. At least 2 rejects?

from math import factorial as fac

p = 0.12
q = 1 - p
n = 10


def binomial(x, n, p):
    return (fac(n) / (fac(x) * fac(n - x))) * (p ** x) * (q ** (n - x))


no_more_than_two_rejects = 0
at_least_two_rejects = 0

for x in range(0, 3):
    no_more_than_two_rejects += binomial(x, n, p)

for x in range(2, n + 1):
    at_least_two_rejects += binomial(x, n, p)


print('{0:.3f}'.format(no_more_than_two_rejects))
print('{0:.3f}'.format(at_least_two_rejects))
