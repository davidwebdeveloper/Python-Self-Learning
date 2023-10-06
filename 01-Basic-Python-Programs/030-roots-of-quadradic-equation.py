# Python example to find Roots of a Quadratic Equation
import math

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))


d = b * b-4 * a * c
print(d)

if (d > 0):
    print(
        f"Root1 = {(-b + math.sqrt(d))/(2*a)}\nRoot2 = {(-b - math.sqrt(d))/(2*a)}")
elif (d == 0):
    print(f"Root1 = Root2 = {-b / 2*a}\n")

else:
    first = -b / 2*a
    second = math.sqrt(-d) / (2*a)
    print(f"Root1 = {first}+{second}i\nRoot2 = {first}-{second}i")
