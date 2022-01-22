"""
Stundents were asked on the final test to find the confidence intervals for a given regression model.
This program helps them to check the pen and paper calculations and check whether their results were correct.
"""

from termcolor import colored

b_value = float(input("Enter b-value "))
stde_value = float(input("Enter se(b) "))
n_value = float(input("Enter n "))
k_value = float(input("Enter k "))

df = (n_value - k_value)
print(colored("Look at the t table two tail at the given confidence interval with the df =","green"), colored(df, "green"))

#Since it is always two tail test consider implementing the T-table instead asking the user
df_table = float(input("Enter value from T-table "))

UB = (b_value + (df_table * stde_value))
LB =  (b_value - (df_table * stde_value))

print(colored("Confidence interval: [", "green"), colored(float(round(LB, 5)), "green"), colored(float(round(UB,5)), "green"), colored("]","green"))

print("_"* 50)
print(colored("Credits: Adam"))