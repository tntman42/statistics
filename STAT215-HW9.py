import math
import stat_math
import calculus_math


def problem1(sample, fails, za_2):
    print("Problem 1")
    successes = sample - fails
    p = successes / sample
    q = 1 - p
    low = p - za_2 * math.sqrt(p * q / sample)
    high = p + za_2 * math.sqrt(p * q / sample)
    print("\t", round(low, 3), " < p < ", round(high, 3))


def problem2(confidence, err):
    print("Problem 2")
    alpha = 1 - confidence
    alpha_2 = alpha / 2
    print("\talpha/2 = ", alpha_2)
    za_2 = stat_math.confidence_z(confidence)
    print("\tz_(alpha/2) = ", za_2)
    n = (za_2 ** 2) / (4 * (err ** 2))
    print("\tSize: ", round(n))


def problem3(ee_n, ee_wom, chem_n, chem_wom, confidence):
    print("Problem 3")
    p_ee = ee_wom / ee_n
    p_chem = chem_wom / chem_n
    q_ee = 1 - p_ee
    q_chem = 1 - p_chem
    dev = math.sqrt((p_ee * q_ee) / ee_n + (p_chem * q_chem) / chem_n)
    print("\tSQRT: ", dev)
    za_2 = stat_math.confidence_z(confidence)
    print("Z_(a/2) = ", za_2)
    low = (p_ee - p_chem) - za_2 * dev
    high = (p_ee - p_chem) + za_2 * dev
    print("\t", round(low, 3), " < p1 - p2 < ", round(high, 3))


if __name__ == "__main__":
    # problem1(900, 27, 2.5813)
    # problem2(0.90, 0.05)
    problem3(225, 90, 150, 40, 0.99)
