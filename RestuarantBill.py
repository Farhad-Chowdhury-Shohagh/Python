foods = []
quantity = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy ( q to quit): ")
    if food.lower()=="q":
        break
    else:
        qt = int(input("Enter the quantity: "))
        price = float(input(f"Enter the price for each {food}: "))
        foods.append(food)
        quantity.append(qt)
        prices.append(price)

print("------- YOUR CART -------")

for i in range(len(foods)):
    print(f"{i+1}. {foods[i]}   {quantity[i]} pc   {prices[i] * quantity[i]:,.2f} tk")
    total = total + quantity[i]*prices[i]

print()
print(f"Total Bill: {total:,.2f} tk")
print()