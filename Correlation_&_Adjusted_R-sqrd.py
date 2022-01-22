#Add description and scope

from termcolor import colored

print("Use this if you want to find the corr and R2 given the Std (for x,y, respectively) and the covariance ")
Sxy = float(input("Enter Sxy (Covariance): "))
Stdx = float(input("Enter Sx, (Stdx): "))
Stdy =float(input("Enter Sy, (Stdy): "))
corr = Sxy/(Stdx * Stdy)

R2 = corr*corr

print(colored("Correlation = ","green"),colored(float(round(corr,5)), "green"))
print(colored("R-sqrd = ","green"), colored(float(round(R2,4)), "green"))

Proportion_variation = round(R2,4) *100
print("Proportion variation explained by ", Proportion_variation, "%" )
choice = input("Do you want the AdjR2? Type Yes/No ")

if choice == "yes":
   n = float(input("Enter n: "))
   k = float(input("Enter k: "))
   AdjR2 = 1-(1-R2)*((n-1)/(n-k))
   print("Adjusted R2 = ", round(AdjR2,4))
else:
  print("Bye")