# Python Program to Print Negative Numbers in a Range

minimum = int(input("Enter the minimum limit: "))
maximum = int(input("Enter the maximum limit: "))

for i in range(minimum, maximum+1):
    if (i < 0):
        print(i, end=" ")
