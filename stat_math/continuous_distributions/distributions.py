import matplotlib.pyplot as plt


def discritize_function(funk, xrange, plot=False):
    x = [x for x in xrange]
    y = [funk(x) for x in xrange]
    if plot:
        plt.plot(x, y)
        plt.show()
    return x, y