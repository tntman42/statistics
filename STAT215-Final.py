import math
from statistics import mean, variance
from scipy.stats import *
import calculus_math
import stat_math


def problem1(tax_free, mutual, both):
    print("Problem 1")
    oor = tax_free + mutual - both
    print("\ta) ", oor)
    print("\tb) ", (1 - oor))


def problem2(h, nh):
    print("Problem 2")
    n = sum(h) + sum(nh)
    print("\ta) ", h[2] / (h[2] + nh[2]))
    print("\tb) ", nh[0] / (sum(nh)))


def problem4(a, b):
    print("Problem 4")
    ra = a / 100
    rb = (b[0] / 100, b[1] / 100)

    res_a = 1 / 2 + ((2 * ra) - ((ra ** 2) / 2) - 1.5)
    print("\ta) ", round(res_a, 3))
    res_b = calculus_math.integral(lambda x: x, rb[0], rb[1])
    print("\tb) ", round(res_b, 3))


def problem6(probs, profits, problem):
    print("Problem ", problem)
    e = 0
    for i in range(len(probs)):
        e += probs[i] * profits[i]
    print("\te: ", e)


def problem7(function, range, unit):
    print("Problem 7")
    e = calculus_math.integral(lambda x: x * function(x), range[0], range[1]) * unit
    print("\te: ", int(round(e)))


def problem8(prob, x):
    print("Problem ", 8)
    e = 0
    e2 = 0
    for i in range(len(prob)):
        e += prob[i] * x[i]
        e2 += prob[i] * x[i] ** 2
    print("\te(x): ", e)
    print("\te(x^2): ", e2)


def problem9(funk, rang):
    print("Problem 9")
    ex = calculus_math.integral(lambda x: x * funk(x), rang[0], rang[1])
    ex2 = calculus_math.integral(lambda x: x ** 2 * funk(x), rang[0], rang[1])
    var = ex2 - ex ** 2
    print("\tvar:", var)


def problem12(prob, n, a, b, c):
    print("Problem 12")
    pa = 0
    for i in range(a[0], a[1] + 1):
        pa += binom.pmf(i, n, prob)
    print("\ta) ", round(pa, 4))
    pb = 0
    for i in range(b):
        pb += binom.pmf(i, n, prob)
    print("\tb) ", round(pb, 4))
    pc = 0
    for i in range(c + 1, n + 1):
        pc += binom.pmf(i, n, prob)
    print("\tc) ", round(pc, 4))


def problem13(p, a):
    print("Problem 13")
    pa = 0
    for i in range(a):
        pa += poisson.pmf(i, p)
    pa = 1 - pa
    print("\ta) ", round(pa, 4))
    pb = poisson.pmf(0, p)
    print("\tb) ", round(pb, 4))


def problem14(lower, upper, check, given):
    print("Problem 14")
    uni = stat_math.UniformDistribution(lower, upper)
    n = calculus_math.integral(lambda x: uni[x], lower, given)
    dx = calculus_math.integral(lambda x: uni[x], check, given)
    p = dx / n
    print("\tp: ", round(p, 4))


def problem15(mea, stdev, a, b, c):
    print("problem 15")
    pa = norm.cdf(a, mea, stdev)
    print("\ta) ", round(pa, 4))
    pb = norm.cdf(b[1], mea, stdev) - norm.cdf(b[0], mea, stdev)
    print("\tb) ", round(pb, 4))
    pc = 1 - norm.cdf(c, mea, stdev)
    print("\tc) ", round(pc, 4))


def problem16(data):
    print("Problem 16")
    mu = mean(data)
    print("\tmx: ", round(mu, 2))
    va = variance(data)
    print("\tvar: ", round(va, 2))


def problem17(mea, stdev, n, a, b, c):
    print("Problem 17")
    za = (a - mea) / (stdev / math.sqrt(n))
    pa = norm.cdf(za, 0, 1)
    print("\ta) ", round(pa, 4))
    zb = (b - mea) / (stdev / math.sqrt(n))
    pb = norm.sf(zb, 0, 1)
    print("\tb) ", round(pb, 4))
    zc = ((c[0] - mea) / (stdev / math.sqrt(n)), (c[1] - mea) / (stdev / math.sqrt(n)))
    pc = norm.cdf(zc[1], 0, 1) - norm.cdf(zc[0], 0, 1)
    print("\tc) ", round(pc, 4))


def problem18(n, mea, stdev, confidance):
    print("Problem 18")
    za_2 = stat_math.confidence_z(confidance)
    a_2 = za_2 * stdev + mea
    low = mea - a_2 * math.sqrt(mea)


def problem20(sample, fails, confidance):
    print("Problem 20")
    za_2 = stat_math.confidence_z(confidance)
    successes = sample - fails
    p = successes / sample
    q = 1 - p
    low = p - za_2 * math.sqrt(p * q / sample)
    high = p + za_2 * math.sqrt(p * q / sample)
    print("\t", round(low, 3), " < p < ", round(high, 3))


def problem22(mea, n, x, stdev):
    print("Problem 22")
    tv = (x - mea) / (stdev / math.sqrt(n))
    print("\tt: ", round(tv, 2))
    p = t.sf(abs(tv), n - 1)
    print("\tp: ", p)
    if p > 0.01:
        print("\tDo not reject")
    else:
        print("\tReject")


def problem23(n0, n1, incr, sdev0, sdev1):
    print("Problem 23")
    sp = math.sqrt(((sdev0 ** 2) * (n0 - 1) + (sdev1 ** 2) * (n1 - 1)) / (n0 + n1 - 2))
    tv = incr / (sp * math.sqrt(1 / n1 + 1 / n0))
    print("\tt = ", round(tv, 2))
    prob = t.sf(abs(tv), n0 + n1 - 2)
    print("\tp = ", prob)
    if prob > 0.01:
        print("\tDo not reject")
    else:
        print("\tReject")


def problem24(x0, n0, x1, n1):
    print("Problem 24")
    up = [x0 / n0, x1 / n1]
    ph = (x0 + x1) / (n0 + n1)
    qh = 1 - ph
    z = (up[0] - up[1]) / math.sqrt(ph * qh * (1 / n0 + 1 / n1))
    print("\tts: ", round(z, 2))
    p = 2 * (1 - norm.cdf(abs(z)))
    print("\tp: ", round(p, 3))
    if p > 0.01:
        print("\tDo not reject")
    else:
        print("\tReject")


def problem25(d0, d1, sig):
    print("Problem 25")
    mat = [d0, d1]
    row_sums = [sum(d0), sum(d1)]
    col_sums = [0, 0, 0]
    for i in range(len(col_sums)):
        col_sums[i] += d0[i]
        col_sums[i] += d1[i]
    n = 0
    for sn in row_sums:
        n += sn
    z = 0
    for i in range(len(row_sums)):
        for j in range(len(col_sums)):
            e = col_sums[j] * row_sums[i] / n
            z += ((mat[i][j] - e) ** 2) / e
    print("\tts: ", round(z, 2))
    dof = (len(row_sums) - 1) * (len(col_sums) - 1)
    prob = chi.sf(z, dof)
    print("\tp: ", prob)
    if prob >= sig:
        print("\tDo not reject")
    else:
        print("\tReject")


if __name__ == '__main__':
    print("Final exam")
    problem1(0.5, 0.6, 0.26)
    problem2([21, 39, 28], [48, 30, 14])
    problem4(130, (60, 85))
    problem6([0.20, 0.48, 0.26, 0.06], [450, 250, 0, -250], 6)
    problem7(lambda x: (12 - x) / 22, (0, 2), 3000)
    problem8([0.46, 0.29, 0.15, 0.08, 0.02], [0, 1, 2, 3, 4])
    problem9(lambda x: (2 * (x + 2)) / 5, (0, 1))
    problem12(0.4, 14, (2, 6), 4, 5)
    problem13(0.9, 2)
    problem14(1, 5, 1.5, 3)
    problem15(20, 1, 19, (18, 20), 21)
    problem16([11.4, 11.2, 9.4, 12.3, 12.2, 14.2, 13.5, 10.9])
    problem17(8.5, 4, 64, 7.6, 9.2, (8.5, 9.0))
    # problem18(15, 80.7, 7.6, 0.90)
    problem20(600, 24, 0.90)
    problem22(40, 66, 38, 6.6)
    problem23(30, 30, 0.322, 0.106, 0.101)
    problem24(66, 100, 46, 80)
    problem25([17, 36, 26], [55, 25, 22], 0.05)
