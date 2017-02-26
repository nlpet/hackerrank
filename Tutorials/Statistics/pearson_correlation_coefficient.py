from math import sqrt


def mean(arr, n):
    return sum(arr) / n


def std(arr, mu, n):
    sum_squared_dist = 0
    for x in arr:
        sum_squared_dist += pow(x - mu, 2)
    sigma = sqrt(sum_squared_dist / n)

    return sigma


# Measure of how two random variables change together and
# the strength of their correlation
def covariance(X, Y, mu_x, mu_y, n):
    sum_covariances = 0
    for i in range(n):
        sum_covariances += (X[i] - mu_x) * (Y[i] - mu_y)

    return sum_covariances / n


def pearson_correlation_coeff(cov):
    return cov / (std_x * std_y)


if __name__ == '__main__':
    N = int(input().strip())
    X = list(map(float, input().strip().split(' ')))
    Y = list(map(float, input().strip().split(' ')))

    mu_x = mean(X, N)
    std_x = std(X, mu_x, N)

    mu_y = mean(Y, N)
    std_y = std(Y, mu_y, N)

    cov = covariance(X, Y, mu_x, mu_y, N)

    print('{:.3f}'.format(pearson_correlation_coeff(cov)))
