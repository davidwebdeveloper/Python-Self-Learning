# Python program to check Number Divisible by 5 and 11
number = int(input("Enter the number: "))
if (number % 5 == 0 and number % 11 == 0):
    print("{} is divisible by 5 and 11".format(number))
else:
    print("{} is not divisbile by 5 and 11".format(number))
