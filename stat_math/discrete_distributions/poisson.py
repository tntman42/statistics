import math


class PoissonDistribution(object):

    def __init__(self, lamb, t):
        self.lamb = lamb
        self.t = t

    def eval(self, x):
        return (math.exp(-self.lamb * self.t) * (self.lamb * self.t) ** x) / math.factorial(x)

    def __getitem__(self, item):
        return self.eval(item)

    def variance(self):
        return self.lamb * self.t

    def expected_value(self):
        return self.lamb * self.t
