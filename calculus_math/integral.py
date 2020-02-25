from .constants import SMALL_VAL
import numpy


def integral(fcn, start, end):
    inc = SMALL_VAL
    sum = 0
    for x in numpy.arange(start + inc, end, inc):
        sum += ((fcn(x - inc) + fcn(x)) / 2) * inc
    return sum