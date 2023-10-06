# Python program to find Power of a Number
import math
number = int(input("Enter the number: "))
power = int(input("Enter the raised to the power number: "))
print("{0} to the power of {1} is = {2}".format(
    number, power, math.pow(number, power)))
