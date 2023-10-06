# Python program to find Largest of 3 Numbers

# Type 1

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if (a > b and a > c):
    print('{0} is larger than{1} and {2}'.format(a, b, c))
elif (b > c and b > a):
    print('{1} is larger than {0} and {1}'.format(a, b, c))
elif (c > a and c > b):
    print('{2} is larger than {1} and {0}'.format(a, b, c))
else:
    print("All the values are equal or two values or equal")
