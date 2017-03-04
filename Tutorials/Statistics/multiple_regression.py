from sklearn import linear_model


m, n = list(map(int, input().strip().split(' ')))
x, y = [], []

for _ in range(n):
    line = list(map(float, input().strip().split(' ')))
    x.append(line[: m])
    y.append(line[m])


lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
coeffs = lm.coef_

q = int(input().strip())

for _ in range(q):
    B = list(map(float, input().strip().split(' ')))
    res = a + sum(map(lambda pair: pair[0] * pair[1], zip(coeffs,B)))
    print('{:.2f}'.format(res))
