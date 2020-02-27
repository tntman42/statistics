from .combinotorics import *


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


class NegativeBinomialDistribution(object):

    def __init__(self, k, p):
        self.k = k
        self.p = p
        self.q = 1 - p

    def eval(self, x):
        return combination(x - 1, self.k - 1) * (self.p ** self.k) * (self.q ** (x - self.k))

    def __getitem__(self, item):
        return self.eval(item)
