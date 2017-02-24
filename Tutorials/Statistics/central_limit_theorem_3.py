from math import sqrt, erf

# Central Limit Theorem
# The central limit theorem (CLT) states that, for a large enough sample (n)
# the distribution of the sample mean will approach normal distribution.
# This holds for a sample of independent random variables from any distribution
# with a finite standard deviation.
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3

if __name__ == '__main__':
    n = 100
    mu = 500
    std = 80
    z = 1.96

    # Confidence interval
    margin_of_error = z * (std / sqrt(n))

    print('{:.2f}'.format(mu - margin_of_error))
    print('{:.2f}'.format(mu + margin_of_error))
