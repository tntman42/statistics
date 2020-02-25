import math


def permutation(n, r):
    return math.factorial(n) / math.factorial(n - r)


def combination(n, r):
    return permutation(n, r) / math.factorial(r)