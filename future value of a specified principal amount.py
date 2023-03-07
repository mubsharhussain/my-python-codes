#Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years
"""
The formula for future value with compound interest is FV = P(1 + r/n)^nt.
FV = the future value;
P = the principal;
r = the annual interest rate expressed as a decimal;
n = the number of times interest is paid each year;
t = time in years.
"""
p=float(input("enter the principal amount ="))
n=float(input("number of times interest is paid each year="))
t=float(input("number of years"))
FV = p*((1 + (0.01*n)))**t
print(FV)
