principle, rate, time =0,0,0

while True:
    principle = float(input("Enter principle amount: "))
    if principle <=0:
        print("Principle amount can't be zero or negative!")
    else:
        break

while True:
    rate = float(input("Enter interest rate: "))
    if rate<0:
        print("Interest cannot be zero or negative!")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time <=0:
        print("Time can't be zero or negative!")
    else:
        break

total = principle*pow((1+rate/100),time)

print(f"Your payable amount after {time} years: {total:,.2f} tk")