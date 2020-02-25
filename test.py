from stat_math.graphing import *
import numpy
import calculus_math


def main():
    print("Starting test")
    discritize_function(lambda x: uniform_function(x, 3, 5), numpy.arange(2, 6, 0.01), plot=True)
    discritize_function(lambda x: normal(x, 0, 1), numpy.arange(-5, 5, 0.01), plot=True)
    print("Finished drawing")
    print(calculus_math.integral(lambda x: normal(x, 0, 1), -1.46, 5))


if __name__ == "__main__":
    main()
    quit()
