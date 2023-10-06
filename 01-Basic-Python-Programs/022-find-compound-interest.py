# Python Program to find Compound Interest

p: float = float(input("Enter the principle amount: "))
n: int = int(input("Number of times intrest calculated by year: "))
r: float = float(input("Rate of intrest: "))
t: float = float(input("How many years: "))

amount: float = p * (1+r/(n*100))**(n*t)


print(amount)
print("Compound intrest is = {}".format(amount-p))
