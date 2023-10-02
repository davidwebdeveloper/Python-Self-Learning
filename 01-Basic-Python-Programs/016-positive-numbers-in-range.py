# Python Program to Print Positive Numbers in a Range
minimum = int(input('Enter the minimum range: '))
maximum = int(input("Enter the maximum range: "))
for i in range(minimum, maximum+1):
    print(i, end=' ')
