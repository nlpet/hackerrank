from math import sqrt, erf
# Task
#
# The final grades for a Physics exam taken by a large group of students have a
# mean of  and a standard deviation of . If we can approximate the distribution
# of these grades by a normal distribution, what percentage of the students:
def cdf(mu, std, x):
    return 0.5 * ( 1 + erf((x - mu) / (std * sqrt(2))))


if __name__ == '__main__':
    mu, std = 70, 10
    x1, x2 = 80, 60

    # Scored higher than 80
    print('{:.2f}'.format(100 * (1 - cdf(mu, std, x1))))
    # Passed the test: grade >= 60
    print('{:.2f}'.format(100 * (1 - cdf(mu, std, x2))))
    # Failed the test: grade < 60
    print('{:.2f}'.format(100 * (cdf(mu, std, x2))))
