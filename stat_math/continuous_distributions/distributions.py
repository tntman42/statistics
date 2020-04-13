from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import calculus_math


def discritize_function(funk, xrange, plot=False):
    x = [x for x in xrange]
    y = [funk(x) for x in xrange]
    if plot:
        plt.plot(x, y)
        plt.show()
    return x, y


class Distribution(ABC):

    @abstractmethod
    def eval(self, x):
        pass

    def __getitem__(self, item):
        return self.eval(item)

    def expected_value(self):
        return calculus_math.integral(lambda x: x * self.eval(x), -1000, 1000, increment=1e-3)

    @abstractmethod
    def variance(self):
        pass

    def draw(self):
        discritize_function(self.eval, range(-100, 100), plot=True)

    def integrate(self, a, b):
        return calculus_math.integral(self.eval, a, b)
