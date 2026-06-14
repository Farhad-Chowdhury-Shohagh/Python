menus = {"coca cola": 40,
         "pepsi": 30,
         "7up": 30,
         "potato": 10,
         "mr twist": 20,
         "lays": 50}
cart = []
total =0

print("----------Menus----------")
for key, values in menus.items():
    print(f"{key:10}: {values:.2f} tk")
print("-------------------------")
print("\n----Place your order----")
while True:
    food = input("Enter an item (or q for quit): ").lower()
    if food == "q":
        break
    elif menus.get(food) is not None:
        cart.append(food)
    else:
        print("Not Available!")

print("-------------------------")
for food in cart:
    total += menus.get(food)
    print(food, end=" ")

print(f"\nTotal: {total:.2f} tk")
