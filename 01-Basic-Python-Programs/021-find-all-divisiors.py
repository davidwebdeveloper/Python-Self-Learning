# Python Program to find all divisors of an integer
number = int(input("Enter the number: "))
for i in range(1, number+1):
    if (number % i == 0):
        print(i, end=" ")
