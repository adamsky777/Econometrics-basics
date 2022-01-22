"""
This tool is designed to help students finding the residuals in a regression model, given two observation data.
"""

from termcolor import colored

b1 = float(input("Enter b1 "))
b2 = float(input("Enter b2 "))
obs_b1 = float(input("Enter b1 observation data "))
obs_b2 = float(input("Enter b2 observation data "))

positive = input(print("Model + / - ? "))
if positive == "+":
    yhat = (b1+ b2 * obs_b2)
    e = (obs_b1 - yhat)
    e = round(e, 4)
    print(colored("residual = ", "green"), colored(e, "green"))
elif positive == "-":
    yhat = (b1 - b2 * obs_b2)
    e = (obs_b1 - yhat)
    e = round(e, 4)
    print(colored("residual = ", "green"), colored(e, "green"))
else:
    print("only ? or - sing")

print("is it measured in 100 or 1000 ? if yes then multiply ", e,"  respectively")


print("_" *50)
print(colored("Credits: Adam", "blue"))