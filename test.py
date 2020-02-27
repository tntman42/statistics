from stat_math.continuous_distributions import *
import calculus_math


def main():

    print(round(calculus_math.integral(z_eval, -1.46, 5), 7))
    print(round(z_integrate(-1.46, 5), 7))


if __name__ == "__main__":
    main()
    quit()
