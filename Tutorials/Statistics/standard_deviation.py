from math import sqrt


def mean(arr, n):
    return sum(arr) / n

if __name__ == '__main__':
    N = int(input().strip())
    X = list(map(int, input().strip().split(' ')))

    mu = mean(X, N)
    sum_squared_dist = 0

    for x in X:
        sum_squared_dist += pow(x - mu, 2)

    sigma = sqrt(sum_squared_dist / N)

    print('{0:0.1f}'.format(sigma))
