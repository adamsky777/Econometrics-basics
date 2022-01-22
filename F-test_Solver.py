"""
Students were asked to test Heteroscedasticity and/or Autocorrelation. Normally the possibility of making mistakes
when carrying out the calculations on pen and paper are quite high. With this tool students were able to test their
calculations quickly. Consequently have gained more time by enabling them to get more knowledge and understanding.
"""

from termcolor import colored
from scipy import stats as st
import os
import sys


def goto(linenum):
    global line
    line = linenum


line = 1
while True:
    if line == 1:
        print("Use this test for heteroscedasticity & Autocorr,  remember R-restricted = 0 in that case")
        R_unrestricted = float(input("Enter R-UNrestriced "))
        print("for heteroscedascticity and autocorr we assueme R-restricted = 0")
        R_restricted = float(input("Enter R-Restricted "))
        n_value = float(input("Enter n "))
        k_value = float(input(" (# of B's in unresrdicted) Enter k "))
        m_value = float(input("Enter m "))

        f_top = ((R_unrestricted - R_restricted) / m_value)
        f_bottom = ((1 - R_unrestricted) / (n_value - k_value))
        F = (f_top / f_bottom)
        print(colored("F-value = ", "green"), colored(round(F, 5), "green"))
        print(colored("F-value = ", "green"), colored(round(F, 2), "green"))
        print(colored("p-value = ", "red"), colored(m_value, "red"))

        h0_test = input("Hypothesis test for the whole model F? \n Type  yes/no ")

        if h0_test == "yes":
            df1 = (m_value)
            df2 = (n_value - k_value)
            print(colored("df1 = ", "red"), colored(float(df1), "red", ), colored("df2 = ", "red"),
                  colored(float(df2), "red"))
            alpha10 = st.f.ppf(q=1 - 0.10, dfn=df1, dfd=df2)
            alpha5 = st.f.ppf(q=1 - 0.05, dfn=df1, dfd=df2)
            alpha1 = st.f.ppf(q=1 - 0.01, dfn=df1, dfd=df2)
            print("F-alpha 10% = ", alpha10, "\n", "F-alpha 5% = ", alpha5, "\n", "F-alpha 1% = ", alpha1, )
        else:
            print("Bye")
            sys.exit()
    if F > alpha10:
        print(colored("Reject H0 at 10%", "green"))
    else:
        print(colored("Can't rejcet at 10% , Keep H0", "green"))
    if F > alpha5:
        print(colored("Reject H0 at 5%", "green"))
    else:
        print(colored("Can't reject at 5%, Keep H0 ", "green"))
    if F > alpha1:
        print(colored("Reject H0 at 1%", "green"))
    else:
        print(colored("Can't reject at 1%, Keep H0", "green"))
    print("Keep = not heteroscedastic")
    print(colored("Credits: Adam ", "yellow"))

    rerun = input("run again? yes/no ")
    if rerun == "yes":
        clear = lambda: os.system('clear')
        clear()
        goto(1)
    else:
        print("Bye")
        sys.exit()