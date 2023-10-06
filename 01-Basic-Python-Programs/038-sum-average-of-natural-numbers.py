# Python example to find Sum and Average of Natural Numbers

limit = int(input("Enter the limit: "))
sumN = 0
for i in range(1, limit+1):
    sumN += i
print(f"sum = {sumN}")
print(f"Avg = {sumN / limit}")
