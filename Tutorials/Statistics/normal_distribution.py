from math import sqrt, pi, e, erf

# Normal Distribution
#
# Probability density of normal distribution
def N(mu, variance, x):
    """
    :mu (int, float) : mean (or expectation) of the distribution
    :variance (int, float): variance
    :x (int, float): random variable
    """
    std = sqrt(variance)
    return (1 / (std * sqrt(2 * pi))) * (e ** (- ((x - mu) ** 2) / (2 * variance)))


# Cumulative Probability
#
# Consider a real-valued random variable, X. The cumulative distribution
# function of X (or just the distribution function of X) evaluated at x is
# the probability that X will take a value less than or equal to x
def cdf(mu, std, x):
    return 0.5 * ( 1 + erf((x - mu) / (std * sqrt(2))))


if __name__ == '__main__':
    mu, std = 20, 2
    x = 19.5
    a, b = 20, 22
    print('{:.3f}'.format(cdf(mu, std, x)))
    print('{:.3f}'.format(cdf(mu, std, b) - cdf(mu, std, a)))
