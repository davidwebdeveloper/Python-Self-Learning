# Python program to find Profit Or Loss

cost_price = float(input('Enter the cost price: '))
selling_price = float(input("Etner the selling price: "))

if (cost_price > selling_price):
    print("loss is {}".format(cost_price-selling_price))
else:
    print("profit is {}".format(selling_price-cost_price))
