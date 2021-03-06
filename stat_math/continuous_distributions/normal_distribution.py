import math
from abc import ABC

import numpy
from .distributions import discritize_function, Distribution
import calculus_math


def z_eval(z):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * (z ** 2))


def erf(x):
    if -5 < x < 5:
        a = 2
        c = 2.4065
        o = a / 2
        return a * (math.exp(c * x) / (math.exp(c * x) + 1)) - o
    else:
        return 2 / math.sqrt(math.pi) * calculus_math.integral(lambda t: math.exp(-t ** 2), 0, x)


def z_integrate(a, b):
    sqrt_half = math.sqrt(0.5)
    sqrt_pih = math.sqrt(math.pi / 2)
    return (1 / math.sqrt(2 * math.pi)) * ((sqrt_pih * erf(sqrt_half * b)) - (sqrt_pih * erf(sqrt_half * a)))


def confidence_z(confidence):
    left = (1 + confidence) / 2
    z = 0
    ar = calculus_math.integral(lambda x: z_eval(x), -5, z)
    incr = 1
    while abs(ar - left) > 0.001:
        if ar < left:
            z += incr
        elif ar > left:
            z -= incr
            incr /= 10
            z += incr
        ar = calculus_math.integral(lambda x: z_eval(x), -5, z)
    ar = calculus_math.integral(lambda x: z_eval(x), -5, z)
    ar1 = calculus_math.integral(lambda x: z_eval(x), -5, z + incr)

    return z if abs(ar - left) < abs(ar1 - left) else z + incr


class NormalDistribution(Distribution):

    def __init__(self, mean, deviation, sample_size=0):
        self.mean = mean
        self.deviation = deviation
        self.sample_size = sample_size

    def variance(self):
        return self.deviation ** 2

    def expected_value(self):
        return self.mean

    def eval(self, x):
        return (1 / (self.deviation * math.sqrt(2 * math.pi))) * math.exp(
            (-1 / (2 * (self.deviation ** 2))) * ((x - self.mean) ** 2))

    def z_score(self, x):
        return (x - self.mean) / self.deviation

    def un_z_score(self, z):
        return self.deviation * z + self.mean

    def draw(self, resolution=0.01):
        discritize_function(lambda x: self[x], numpy.arange(self.mean - self.deviation * 4,
                                                            self.mean + self.deviation * 4, resolution), plot=True)

    def sample_mean(self, sample_size):
        return NormalDistribution(self.mean, self.deviation / math.sqrt(sample_size), sample_size)
