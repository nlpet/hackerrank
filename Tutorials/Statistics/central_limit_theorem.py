from math import sqrt, erf

# Central Limit Theorem
# The central limit theorem (CLT) states that, for a large enough sample (n)
# the distribution of the sample mean will approach normal distribution.
# This holds for a sample of independent random variables from any distribution
# with a finite standard deviation.
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1

def cdf(mu, std, x):
    return 0.5 * (1 + erf((x - mu) / (std * sqrt(2))))


if __name__ == '__main__':
    maxn = 9800
    n = 49
    mu = 205
    std = 15
    mup = n * mu
    stdp = sqrt(n) * std
    print('{:.4f}'.format(cdf(mup, stdp, maxn)))
