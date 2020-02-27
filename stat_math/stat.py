
def cdf(funk, xrange):
    prob = 0
    for x in xrange:
        prob += funk(x, *params)
    return prob


def expected_value(funk, xrange):
    val = 0
    for x in xrange:
        val += x * funk(x)
    return val

