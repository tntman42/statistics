import math
from .distributions import Distribution


class ExponentialDistribution(Distribution):

    def __init__(self, beta):
        self.beta = beta

    def eval(self, x):
        if x > 0:
            return 1 / self.beta * math.exp(-x / self.beta)
        else:
            return 0

    def variance(self):
        return self.beta ** 2

    def expected_value(self):
        return self.beta

    def integrate(self, a, b):
        return -(self.eval(b) - self.eval(a))
