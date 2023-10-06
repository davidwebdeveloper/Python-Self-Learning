# Python Program to Find Sum of 10 Numbers until user enters Positive Numbers
sumN = 0
for i in range(1, 11):
    n = int(input(f"Enter number {i}:"))
    if (n > 0):
        break
    sumN += n
print(f"Sum = {sumN}")
