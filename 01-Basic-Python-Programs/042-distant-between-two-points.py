# Python Program to Find Distance Between Two Points
# Distance between two points is d = sqrt((x2-x1)**2+(y2-y1)**2)
import math

x1 = float(input("Enter the x coordinate of point 1 = "))
y1 = float(input("Enter the y coordinate of point 1 = "))
x2 = float(input("Enter the x coordinate of point 2 = "))
y2 = float(input("Enter the y coordinate of point 2 = "))

d = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f"Distance is = {d} units")
