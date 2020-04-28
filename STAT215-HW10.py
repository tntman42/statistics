import math
from scipy.stats import t
from statistics import mean, stdev


def problem1(mean, xbar, stddev, size):
    print("Problem 1")
    tv = (xbar - mean) / (stddev / math.sqrt(size))
    print("\tt = ", round(tv, 2))
    dof = size - 1
    prob = t.sf(abs(tv), dof)
    print("\tp = ", round(prob, 2))


def problem2(mean, stddev, n_samp, x_bar):
    print("Problem 2")
    tv = (x_bar - mean) / (stddev / math.sqrt(n_samp))
    print("\tt = ", round(tv, 2))
    p = t.sf(abs(tv), n_samp - 1)
    print("\tp = ", round(p, 3))


def problem3(n0, n1, incr, sdev0, sdev1):
    print("Problem 3")
    sp = math.sqrt(((sdev0 ** 2) * (n0 - 1) + (sdev1 ** 2) * (n1 - 1)) / (n0 + n1 - 2))
    tv = incr / (sp * math.sqrt(1 / n1 + 1 / n0))
    print("\tt = ", round(tv, 2))
    prob = t.sf(abs(tv), n0 + n1 - 2)
    print("\tp = ", prob)


def problem4(x0, x1, s0, s1, n0, n1):
    print("Problem 4")
    sp = math.sqrt(((s0 ** 2) * (n0 - 1) + (s1 ** 2) * (n1 - 1)) / (n0 + n1 - 2))
    tv = (x0 - x1) / (sp * math.sqrt(1 / n1 + 1 / n0))
    print("\tt = ", round(tv, 2))
    prob = t.sf(abs(tv), n0 + n1 - 2) * 2
    print("\tp = ", prob)
    print("\tDo not reject, is insufficient, a")


def problem5(xray, chem, lo_sig):
    print("Problem 5")
    d = mean(xray) - mean(chem)
    sd = math.sqrt(abs((stdev(xray) ** 2) / len(xray) - (stdev(chem) ** 2) / len(chem)))
    n_diff = 0
    for i in range(len(xray)):
        if xray[i] != chem[i]:
            n_diff += 1

    tv = d / (sd / math.sqrt(n_diff))
    print("\tt = ", tv)


if __name__ == "__main__":
    print("HW 10")
    problem1(38, 37, 8.4, 64)
    problem2(800, 45, 25, 787)
    problem3(35, 35, 0.338, 0.106, 0.102)
    problem4(38300, 40200, 5200, 5900, 12, 12)
    problem5([1.9, 1.9, 2.3, 2.1, 2.4],
             [2.3, 1.8, 2.4, 2.4, 2.4],
             0.1)
