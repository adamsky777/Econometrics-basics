"""
Stundent T test
"""

from termcolor import colored
n_value = float(input("Enter n "))
k_value = float(input("Enter k "))
b_value = float(input("Enter b-value " "\n pay attention for the MINUS if in the model \n "))
stde_value = float(input("Enter se(b) " "\n pay attention if you added minus before add MINUS here too \n "))
test_value =float(input("Enter test value in H0 "))

increase = float(input("If increase type 1, if decrease type 0 "))

if increase ==1:
    top = (b_value - test_value)
else:
    top = (b_value + test_value)

T = (top / stde_value)


print(colored("T value = ", "green"), colored(round(T, 4), "green"))

T_test = input(" T- test ? show df for p-value (hint: use calculator) Type yes/no ")
twotail = input("two tail?, yes/no?")

if twotail == "yes":
  T = T*(-1)
  print("T-value absolute, since it is two tailed test ")
  print(T)
else:
  T = T
df = (n_value - k_value)

if T_test == "yes":
    print(colored("df =  ", "red"), colored(df, "red"))
    alpha10 = float(input("Enter  10% alpha value "))
    alpha5 = float(input("Enter  5% alpha value "))
    alpha1 = float(input("Enter 1% alpha value "))
else: print("Bye")

if T > alpha10:
    print(colored("Reject H0 at 10%", "green"))
else:
    print(colored("Can't reject, Keep H0 at 10%", "green"))
if T > alpha5:
    print(colored("Reject H0 at 5%", "green"))
else:
    print(colored("Can't reject, Keep H0 at 5%", "green"))
if T > alpha1:
    print(colored("Reject H0 at 1%", "green"))
else:
    print(colored("Can't reject, Keep H0 at 1%", "green"))

print("_"*50)
print(colored("credits: Adam", "yellow"))