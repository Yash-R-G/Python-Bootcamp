#  Shoping cart program
title1 = "Vmax Store"
title2 = "Your Cart"
width = 55
price_col_width = 14

foods = []
prices = []
total = 0

print("=" * width)
print(f"{title1:-^{width}}")
print("=" * width)

while True:
    food = input("Enter the item you want to buy, press q to quit : ")
    if food.lower() == "q":
        break
    price = float(input(f"Enter the price of {food}\n: ₹ "))
    foods.append(food)
    prices.append(price)

print("=" * width)
print(f"{title2:-^{width}}")
print("=" * width)
print()

for food, price in zip(foods, prices):
    price_str = f"₹ {price:,.2f}"
    print(f"{food.title():<{width - price_col_width}} {price_str:>{price_col_width - 1}}")
    total += price

print()
total_str = f"₹ {total:,.2f}"
print(f"{'Your total is :':<{width - price_col_width}} {total_str:>{price_col_width - 1}}")
# print(f"{'Your total is :':<{width - price_col_width}} {total:>{price_col_width - 1},.2f}")
print()
print("=" * width)   
