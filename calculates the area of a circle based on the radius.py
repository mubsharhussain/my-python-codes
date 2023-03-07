"""
Write a Python program that calculates the area of a circle based on the radius entered by the user. 
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
from math import pi#if you want to use pi then you need to impoet math library
r=(float(input("enter the radious of the circule")))
area=pi*r**2
print(area)