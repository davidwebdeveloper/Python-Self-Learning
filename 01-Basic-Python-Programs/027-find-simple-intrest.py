# Python example to find Simple Interest


principle = int(input("Enter the principle amount: "))
years = int(input("Enter the number of year: "))
r = int(input("Enter the rate of intrest: "))

si = (principle * years * r) / 100
print("Simple interest is = {}".format(si))
