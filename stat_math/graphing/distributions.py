import matplotlib.pyplot as plt
import math


def uniform_function(x, lower, upper):
    return 1 / (upper - lower) if lower <= x <= upper else 0


def uniform_expected(lower, upper):
    return (lower + upper) / 2


def uniform_variance(lower, upper):
    return ((upper - lower) ** 2) / 12


#################################################################

def normal(x, mean, deviation):
    return (1 / (deviation * math.sqrt(2 * math.pi))) * math.exp((-1 / (2 * (deviation ** 2))) * ((x - mean) ** 2))

#################################################################


def discritize_function(funk, xrange, plot=False):
    x = [x for x in xrange]
    y = [funk(x) for x in xrange]
    if plot:
        plt.plot(x, y)
        plt.show()
    return x, y