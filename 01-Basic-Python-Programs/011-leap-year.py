# Python program for Leap Year


year = int(input("Enter the year: "))
if (year % 100 == 0):
    if (year % 400 == 0):
        print("{} is leap year".format(year))
    else:
        print("{} is not a leap year".format(year))
elif (year % 4 == 0):
    print("{} is leap year".format(year))
else:
    print("{} is not a leap year".format(year))
