from datetime import datetime


name = input("Enter your name: ")
dob_input = input("Enter your date of birth(DD-MM-YY): ")

dob = datetime.strptime(dob_input, "%d-%m-%Y")

today = datetime.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -=1

print("Your name is "+name)
print(f"You are {age} years old.")