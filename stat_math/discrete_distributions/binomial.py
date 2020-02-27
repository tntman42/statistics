from .combinotorics import *
from stat_math.stat import expected_value
from stat_math.continuous_distributions import *


class BinomialDistribution(object):

    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.q = 1 - p

    def eval(self, x):
        return combination(self.n, x) * (self.p ** x) * (self.q ** (self.n - x))

    def __getitem__(self, item):
        return self.eval(item)

    def variance(self):
        return self.n * self.p * self.q

    def approximate_normal(self):
        if self.n * self.p > 5 and self.n * self.q > 5:
            mean = expected_value(self.eval, range(self.n))
            deviation = math.sqrt(self.variance())
            return NormalDistribution(mean, deviation)
        else:
            raise Exception("Cannot make a small binomial into a normal distribution.")

    def normal_eval(self, x):
        return z_integrate()


class NegativeBinomialDistribution(object):

    def __init__(self, k, p):
        self.k = k
        self.p = p
        self.q = 1 - p

    def eval(self, x):
        return combination(x - 1, self.k - 1) * (self.p ** self.k) * (self.q ** (x - self.k))

    def __getitem__(self, item):
        return self.eval(item)
