
p = 1 / 3
n = 5


def g(n, p):
    return ((1 - p) ** (n - 1)) * p


defect_during_first_five_inspections = sum(g(i, p) for i in range(1, 6))

print('{0:.3f}'.format(defect_during_first_five_inspections))
