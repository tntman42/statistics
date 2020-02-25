
def cdf(funk, xrange, params):
    prob = 0
    for x in xrange:
        prob += funk(x, *params)
    return prob


def expected_value(funk, xrange, params):
    val = 0
    for x in xrange:
        val += x * funk(x, *params)
    return val

