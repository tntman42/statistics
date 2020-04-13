import math
import calculus_math
from .distributions import Distribution


def gamma_function(alpha):
    if alpha > 0:
        return calculus_math.integral(lambda x: x ** (alpha - 1) * math.exp(-x), 0, 1000)
    else:
        return 0


class GammaDistribution(Distribution):

    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def eval(self, x):
        if x > 0:
            return 1 / (self.beta ** self.alpha * gamma_function(self.alpha)) * \
                   x ** (self.alpha - 1) * math.exp(-x / self.beta)
        else:
            return 0

    def variance(self):
        return self.alpha * self.beta ** 2

    def expected_value(self):
        return self.alpha * self.beta
