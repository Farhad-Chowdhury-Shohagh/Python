foods = []
quantitys = []
prices = []
totals = 0

while True:
    food = input("Enter a food to buy (or q to quit): ")
    if food == 'q':
        break
    else:
        quantity = int(input("Enter the quantity of the food: "))
        price = float(input("Enter the price of the food: "))
        foods.append(food)
        quantitys.append(quantity)
        prices.append(price)

print("---------- Your Cart ----------")
for x in range(len(foods)):
    print(f"{x+1}. {quantitys[x]} x {foods[x]}   price: {quantitys[x]} x {prices[x]} tk")
    totals = totals + prices[x]*quantitys[x]

print(f"Your total amount: {totals} tk")
