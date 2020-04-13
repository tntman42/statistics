from .constants import SMALL_VAL
import numpy


def integral(fcn, start, end, increment=SMALL_VAL):
    inc = increment
    su = 0
    for x in numpy.arange(start + inc, end, inc):
        if fcn(x) > inc:
            su += ((fcn(x - inc) + fcn(x)) / 2) * inc
    return su
