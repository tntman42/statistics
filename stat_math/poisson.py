import math


def poisson_distribution(x, lamb, t):
    return (math.exp(-lamb * t) * (lamb * t) ** x) / math.factorial(x)


def poisson_variance(lamb, t):
    return lamb * t


def poisson_expected_value(lamb, t):
    return lamb * t
