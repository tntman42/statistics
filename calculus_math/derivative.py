from .constants import SMALL_VAL


def derivative(fcn, x):
    val = fcn(x)
    lx = x - SMALL_VAL
    lval = fcn(lx)
    rx = x + SMALL_VAL
    rval = fcn(rx)

    sls = (rval - lval) / (rx - lx)
    sll = (val - lval) / (x - lx)
    slr = (rval - rval) / (rx - x)
    return (sls + sll + slr) / 3
