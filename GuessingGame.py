secretWord = "Japan"
chances = 5
guessAdd=[]
done = False
print("-------   Country Guessing Game   -------\nClue: Asian\n")

while not done:
    for letter in secretWord:
        if letter.lower() in guessAdd:
            print(letter, end=" ")
        else:
            print("_", end="")

    guess = input(f"Your remaining chances is {chances}, Guess the letter: ")
    guessAdd.append(guess.lower())

    if guess.lower() not in secretWord.lower():
        chances-=1
        if chances==0:
            break

    done = True
    for letter in secretWord:
        if letter.lower() not in guessAdd:
            done = False

if done:
    print(f"Guess is correct! You Won the game. The word is {secretWord}")
else:
    print(f"You lose the game! The word is {secretWord}")
