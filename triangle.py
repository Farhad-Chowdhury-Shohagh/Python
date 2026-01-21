
rows = int(input("Enter rows number: "))
columns = int(input("Enter columns number: "))
symbol = input("Enter the symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
print()

for i in range(rows):
    for j in range(i+1):
        print(symbol, end="")
    print()
print()

for i in range(rows):
    for j in range(rows-i-1):
        print(" ", end="")
    for k in range(i+1):
        print(symbol+" ", end="")
    print()


print()

for i in range(rows):
    for j in range(i):
        print(" ", end="")
    for k in range(rows-i):
        print(symbol+" ", end="")
    print()
print()

for i in range(rows):
    print(" " * (rows-i), end="")
    coef = 1
    for j in range(i+1):
        print(coef, end=" ")
        coef = coef * (i-j) // (j+1)
    print()
print()

for i in range(rows):
    for j in range(rows):
        print(symbol, end="")
    rows-=1
    print()
print()

