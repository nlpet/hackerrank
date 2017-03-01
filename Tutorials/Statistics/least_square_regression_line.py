"""
Task
A group of five students enrolls in Statistics immediately after taking a Math
aptitude test. Each student's Math aptitude test score, , and Statistics course
grade, , can be expressed as the following list of  points:

95 85
85 95
80 70
70 65
60 70

If a student scored an  on the Math aptitude test, what grade would we expect
them to achieve in Statistics? Determine the equation of the best-fit line
using the least squares method, then compute and print the value of when .
"""

def get_b(X, Y, n):
    numer = n * sum(map(lambda p: p[0]*p[1], zip(X,Y))) - (sum(X) * sum(Y))
    denom = n * sum(map(lambda x: x * x, X)) - (sum(X) ** 2)
    return numer / denom

# Yi = a + bXi
def get_a(X, Y, b, n):
    mean_x = sum(X) / n
    mean_y = sum(Y) / n
    return mean_y - b * mean_x


if __name__ == '__main__':
    N = 5
    given_x = 80
    X, Y = [], []

    for _ in range(N):
        x, y = input().strip().split(' ')
        X.append(int(x))
        Y.append(int(y))

    b = get_b(X, Y, N)
    a = get_a(X, Y, b, N)
    print('{:0.3f}'.format(a + b * given_x))
