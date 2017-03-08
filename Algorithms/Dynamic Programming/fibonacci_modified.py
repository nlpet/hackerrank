import functools


@functools.lru_cache(None)
def fib_mod(n, f, s):
    if n == 1:
        return f
    elif n == 2:
        return s
    else:
        return fib_mod(n - 2) + fib_mod(n - 1) ** 2


f, s, n = list(map(int, input().strip().split(' ')))
print(fib_mod(n, f, s))
