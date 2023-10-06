# Python Program to Find Sum of 10 Numbers and Skip Negative Numbers

# For input 10 numbers
sumN = 0
for i in range(1, 11):

    n = int(input(f"Enter the number {i}: "))
    if (n > 0):
        sumN += n

print(sumN)
