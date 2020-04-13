import stat_math as st
import calculus_math as calc


def problem_1():
    print("Problem 1")
    uni = st.UniformDistribution(1, 5)
    print("\t" + str(uni.integrate(2, 3)))


def problem_2():
    print("Problem 2")
    print("\tPart a")
    uni = st.UniformDistribution(8, 11)
    print("\t\t" + str(uni.integrate(8, 9.8)))
    print("\tPart b")
    print("\t\t" + str(uni.integrate(8.3, 9.8)))
    print("\tPart c")
    print("\t\t" + str(uni.integrate(9.8, 11)))


def problem_3():
    print("Problem 3")
    print("\tPart a")
    print("\t\t" + str(round(calc.integral(lambda x: st.z_eval(x), -5, -1.42), 4)))
    print("\tPart b")
    print("\t\t" + str(round(calc.integral(lambda x: st.z_eval(x), 1.78, 5), 4)))
    print("\tPart c")
    print("\t\t" + str(round(calc.integral(lambda x: st.z_eval(x), -2.21, -0.61), 4)))
    print("\tPart d")
    print("\t\t" + str(round(calc.integral(lambda x: st.z_eval(x), -5, 1.37), 4)))
    print("\tPart e")
    print("\t\t" + str(round(calc.integral(lambda x: st.z_eval(x), -0.88, 5), 4)))
    print("\tPart f")
    print("\t\t" + str(round(calc.integral(lambda x: st.z_eval(x), -0.52, 1.63), 4)))


def problem_5():
    print("Problem 5")
    norm = st.NormalDistribution(15, 2.5)
    print("\tPart a")
    print("\t\t" + str(round(calc.integral(norm.eval, -12.5, 11), 4)))
    print("\tPart b")
    # found value in table
    print("\t\t" + str(round(norm.un_z_score(-0.88), 2)))
    print("\tPart c")
    # Found value in table
    print("\t\t" + str(round(norm.un_z_score(0.56), 2)))
    print("\tPart d")
    print("\t\t" + str(round(calc.integral(norm.eval, 9, 19), 4)))


def problem_6():
    print("Problem 6")
    norm = st.NormalDistribution(19, 1)
    print("\tPart a")
    print("\t\t" + str(round(calc.integral(norm.eval, 14, 18), 4)))
    print("\tPart b")
    print("\t\t" + str(round(calc.integral(norm.eval, 17, 19), 4)))
    print("\tPart c")
    print("\t\t" + str(round(calc.integral(norm.eval, 20, 24), 4)))


def problem_7():
    print("Problem 7")
    norm = st.NormalDistribution(119, 13)
    z = norm.z_score(99)
    amt = calc.integral(st.z_eval, -10, z)
    print("\t" + str(round(550 * amt - 2)))


if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_5()
    problem_6()
    problem_7()
    quit()
