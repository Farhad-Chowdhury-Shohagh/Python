print("Log In\nto your bKash account\n")
print("Account Number")
acc_num = 1675464308
print(f"+88 0{acc_num}\n")

bKash_PIN = 1234
attempts = 2
login_attempts = True
balance = 10000
number = 0
amount = 0
tAmount = 0
PIN = 0

historyNumber = []
historyType = []
historyAmount = []


def sucMsg():
    global bKash_PIN
    global PIN
    while True:
        PIN = int(input("Enter the PIN: "))
        if bKash_PIN == PIN:
            if choice == 2:
                historyAmount.append(amount)
                historyType.append("Send Money")
                historyNumber.append(number)
                print("Send money successful.")
            elif choice == 3:
                historyAmount.append(amount)
                historyType.append("Mobile Recharge")
                historyNumber.append(number)
                print("Mobile recharge successful")
            elif choice == 4:
                historyAmount.append(amount)
                historyType.append("Cash Out")
                historyNumber.append(number)
                print("Cash out successful")
            elif choice == 5:
                historyAmount.append(amount)
                historyType.append("Make Payment")
                historyNumber.append(number)
                print("Payment successful")
            break
        else:
            print("Invalid PIN")



def recNum(choice):
    global amount
    global balance
    global tAmount
    global number
    while True:
        if choice == 2 or choice == 3:
            number = input("Enter the Number: ")
        elif choice == 4:
            number = input("Enter the Agent Number: ")
        elif choice == 5:
            number = input("Enter the Merchant Number: ")
        else:
            print("Invalid choice!")

        if len(number) == 11 and number.startswith("01") and number.isdigit():
            break
        else:
            print("Invalid Number")
    while True:
        amount = float(input("Enter the amount: "))
        if 1 <= amount <= balance:
            if choice == 2:
                if balance >= amount+5:
                    tAmount = amount + 5
                    print(f"Amount: {amount} Charges: + 5 tk Total: {tAmount} tk")
                    balance = balance - tAmount
                    print(f"Available Balance: {balance} tk")
                    sucMsg()
                else:
                    print("Not enough money!")
            elif choice == 3:
                balance = balance - amount
                print(f"Available Balance: {balance} tk")
                sucMsg()
            elif choice == 4:
                if balance >= amount+(amount*0.02):
                    tAmount = amount+(amount*0.02)
                    print(f"Amount: {amount} Charges: 2% tk Total: {tAmount} tk")
                    balance = balance - tAmount
                    print(f"Available Balance: {balance} tk")
                    sucMsg()
                else:
                    print("Not enough money!")
            elif choice == 5:
                balance = balance - amount
                print(f"Available Balance: {balance} tk")
                sucMsg()
            break
        else:
            print("Your Balance is low!")



while login_attempts:
    PIN = int(input("Enter bKash PIN: "))
    if bKash_PIN == PIN:
        while True:
            print("\nbKash\n""1. See Balance\n""2. Send Money\n""3. Mobile Recharge\n""4. Cash Out\n""5. Payment\n""6. History\n""7. Exit")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                print(f"Balance: {balance} tk")
            elif choice == 2:
                recNum(choice)
            elif choice == 3:
                recNum(choice)
            elif choice == 4:
                recNum(choice)
            elif choice == 5:
                recNum(choice)
            elif choice == 6:
                print("\n------------- History of previews transaction -------------")
                for x in range(len(historyNumber)):
                    print(f"Number: {historyNumber[x]} | Type: {historyType[x]} | Amount: {historyAmount[x]}")
            elif choice == 7:
                print("Exit!")
                break
            else:
                print("Invalid Choice!")
        break
    else:
        if attempts != 0:
            print("Invalid PIN. Enter Correct PIN for login")
            attempts = attempts - 1
            print(f"Attempts remaining {attempts+1}")
        else:
            print("Your bKash account has been locked. Please contact customer service.")
            login_attempts = False
