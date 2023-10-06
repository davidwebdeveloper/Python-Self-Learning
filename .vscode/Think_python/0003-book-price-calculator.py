#  What is the volume of sphere? when radius is 5

pi = 3.14
r = 5
volume = 4/3 * pi * r**2
print(volume)


# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. What is
# the total wholesale cost for 60 copies?
no_of_copies = 60
coverPrice = 24.95
discount = coverPrice / 100 * 40
shipping_cost = 3 + (no_of_copies-1)*0.75
book_price = coverPrice - discount
whole_sale_cost = book_price * no_of_copies + shipping_cost
print(f'cover price = {coverPrice}')
print(f"disocunt = {discount}")
print(f"one book total cost = ", book_price)
print(f'Shipping cost = {shipping_cost}')
print(f'Whole sale cost = {whole_sale_cost}')
