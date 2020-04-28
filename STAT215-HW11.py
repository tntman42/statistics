import math
from scipy.stats import *


def problem1(p, n, s, sig):
    print("Problem 1")
    up = s / n
    print("px: ", up)
    prob = 2 * (1 - binom.cdf(s - 1, n, p))
    print("\tp-value: ", round(prob, 3))
    if prob > sig:
        print("\tDo not reject")
    else:
        print("\tReject")


def problem2(p, n, x, sig):
    print("Problem 2")
    up = x / n
    z = (up - p) / (math.sqrt((p * (1 - p)) / n))
    print("\tts: ", round(z, 2))
    prob = 2 * (1 - binom.cdf(x - 1, n, p))
    if prob > sig:
        print("\tDo not reject")
    else:
        print("\tReject")


def problem3(x0, n0, x1, n1):
    print("Problem 3")
    up = [x0 / n0, x1 / n1]
    ph = (x0 + x1) / (n0 + n1)
    qh = 1 - ph
    z = (up[0] - up[1]) / math.sqrt(ph * qh * (1 / n0 + 1 / n1))
    print("\tts: ", round(z, 2))
    p = 2 * (1 - norm.cdf(abs(z)))
    print("\tp: ", round(p, 3))


def problem4(data, sig):
    print("Problem 4")
    n = sum(data)
    z = 0
    e = n / 6.0
    for dat in data:
        z += ((dat - e) ** 2) / e
    print("\tts: ", round(z, 2))
    prob = chi.sf(z, n - 1)
    if prob > sig:
        print("\tDo not reject")
    else:
        print("\tReject")


def problem5(d0, d1, sig):
    print("Problem 5")
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


def problem6(no, some, tot, sig=0.10):
    print("Problem 6")
    mat = [no, some, tot]
    row_sums = [sum(no), sum(some), sum(tot)]
    col_sums = [0, 0, 0]
    for i in range(len(col_sums)):
        col_sums[i] += no[i]
        col_sums[i] += some[i]
        col_sums[i] += tot[i]
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


if __name__ == "__main__":
    print("HW 11")
    problem1(0.5, 20, 14, 0.01)
    problem2(0.33, 86, 35, 0.01)
    problem3(61, 100, 69, 125)
    problem4([68, 65, 48, 57, 61, 49], 0.01)
    problem5([26, 35, 26], [43, 31, 23], 0.01)
    problem6([11, 14, 9], [33, 29, 26], [8, 9, 11])
