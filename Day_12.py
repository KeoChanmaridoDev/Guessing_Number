from ascii import art
import random
easy = 10
hard = 5
print(art)
computerRandom  = random.randint(1,100)
while True:
    print("Welcome to guessing game!")
    print("I'm thinking of number between 1 and 100!")
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    user_done = True
    while True:
        if difficulty in ("easy", "hard"):
            break
        else:
            print("Sorry, that's not a valid difficulty.")
            difficulty = input("Choose a difficulty level: ").lower()
    if difficulty == "easy":
        live = easy
    else:
        live = hard

    while live > 0:
        userGuess = int(input("Guess the number: "))
        if userGuess != computerRandom:
            live -=1
            print(f"You have {live} guess left!")
        if userGuess < computerRandom:
            print("Too low.")
        elif userGuess > computerRandom:
            print("Too high.")
        elif live == 0:
            print("Game over.")
            break
        else:
            print("That's right!")
            break
    while True:
        again = input("Do you want to play again? (y/n): ").lower()
        if again in ("y", "n"):
            break
        else:
            print("Sorry, that's not a valid answer.")
            again = input("Do you want to play again? (y/n): ").lower()

    if again == "y":
        continue
    else:
        break







