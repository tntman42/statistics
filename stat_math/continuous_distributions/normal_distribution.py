import math
import numpy
from .distributions import discritize_function


def z_eval(z):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * (z ** 2))


class NormalDistribution(object):

    def __init__(self, mean, deviation):
        self.mean = mean
        self.deviation = deviation

    def eval(self, x):
        return (1 / (self.deviation * math.sqrt(2 * math.pi))) * math.exp((-1 / (2 * (self.deviation ** 2))) * ((x - self.mean) ** 2))

    def z_score(self, x):
        return (x - self.mean) / self.deviation

    def un_z_score(self, z):
        return self.deviation * z + self.mean

    def __getitem__(self, item):
        return self.eval(item)

    def draw(self, resolution=0.01):
        discritize_function(lambda x: self[x], numpy.arange(self.mean - self.deviation * 4,
                                                            self.mean + self.deviation * 4, resolution), plot=True)
