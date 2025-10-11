import random

RandomNumber = random.randrange(1,100)

print("Note: Total number of guess: 7")
count = 7

i=0
while(i<7):
    guess = int(input("Enter guess(0-100): "))

    if guess > RandomNumber:
        print("The number is too high!")

    elif guess < RandomNumber:
        print("The number is too low!")

    else:
        print("Match! Congratulation, Your guess is correct.")
        break

    count -=1
    print(f"Remaining Guess: {count}")
    i+=1

if guess != RandomNumber:
    print(f"The Random Number is: {RandomNumber}")
