from .combinotorics import *


def binomial_distribution(x, n, p):
    return combination(n, x) * (p ** x) * ((1 - p) ** (n - x))


def binomial_variance(n, p):
    return n * p * (1 - p)


def negative_binomial_distribution(x, k, p):
    q = 1 - p
    return combination(x - 1, k - 1) * (p ** k) * (q ** (x - k))

