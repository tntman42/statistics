from .distributions import discritize_function
import numpy


class UniformDistribution(object):

    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def eval(self, x):
        return (1 / (self.upper - self.lower)) if self.lower <= x <= self.upper else 0

    def __getitem__(self, item):
        return self.eval(item)

    def expected_value(self):
        return (self.lower + self.upper) / 2

    def variance(self):
        return ((self.upper - self.lower) ** 2) / 12

    def __str__(self):
        return "Uniform:(" + str(self.lower) + ", " + str(self.upper) + ")"

    def integrate(self, a, b):
        return (b - a) / (self.upper - self.lower)

    def draw(self, resolution=0.01):
        margin = (self.upper - self.lower) / 10
        discritize_function(lambda x: self[x], numpy.arange(self.lower - margin, self.upper + margin, resolution), plot=True)
