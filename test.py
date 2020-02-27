from stat_math.continuous_distributions import *
import calculus_math


def main():
    norm = NormalDistribution(0, 3)
    norm.draw()

    print(round(calculus_math.integral(z_eval, -1.46, 5), 4))


if __name__ == "__main__":
    main()
    quit()
