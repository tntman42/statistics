import math
from .gamma_distribution import gamma_function
from .distributions import Distribution


class ChiSquaredDistribution(Distribution):

    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def variance(self):
        pass

    def eval(self, x):
        pass
