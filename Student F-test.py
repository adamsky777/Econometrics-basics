"""
F-test for the whole model.

Use this when you test the whole model.
"""

from termcolor import colored
from scipy import stats as st
n_value = float(input("Enter n "))
k_value = float(input("Enter k "))
r_sqrd = float(input("Enter R-sqrd "))
adj = float(-1)
adjk_value = (k_value + adj)

#### EQUATION for F-value
f_top = (r_sqrd / adjk_value)
f_bottom1 = (1 - r_sqrd)
f_bottom2 = (n_value - k_value)
F = (f_top /  (f_bottom1 / f_bottom2))

print(colored("F-value = ", "green"),colored(round(F, 3), "green"))

#Adjusted R-square calcuation

front = 1
mid = (1 - r_sqrd)
back = ((n_value -1) / (n_value - k_value))

Adj_R_sqrd = (front - (mid * back))


print(colored("Adjusted R squared = ", "green"), colored(round(Adj_R_sqrd, 3), "green"))



#Hypothesis test
h0_test = input("Hypothesis test for the whole model F? \n Type  yes/no ")
if h0_test == "yes":
    df1 = (k_value - 1)
    df2 = (n_value - k_value)
    print(colored("df1 = ", "red"), colored(float(df1), "red") , colored("df2 = ", "red"), colored(float(df2), "red"))
    alpha10 = st.f.ppf(q=1-0.10, dfn=df1, dfd=df2)
    alpha5 = st.f.ppf(q=1-0.05, dfn=df1, dfd=df2)
    alpha1 = st.f.ppf(q=1-0.01, dfn=df1, dfd=df2)
    print("F-alpha 10% = ",alpha10,"\n", "F-alpha 5% = ",alpha5 ,"\n","F-alpha 1% = ", alpha1,)
else:
  print("Bye")

if F > alpha10:
    print(colored("Reject H0 at 10%","green"))
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

print(50*"_")
print(colored("credits: Adam", "yellow"))

