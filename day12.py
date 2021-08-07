#1/08/21 
import random
EASY = 10
HARD = 5
def check(guess, number, turns):
    if number > guess:
        print("Too low!")
        return turns-1
    elif number < guess:
        print("Too high!")
        return turns-1
    else:
        print(f"That's right, You did it! The number is {number}")

print("Welcome to the number Guessing game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose the difficulty level. Type 'easy or 'hard': ")
number = random.randint(1, 100)
if level == "easy":
    print("You have 10 attempts to guess the number.")
    guess = 0
    while guess != number:
        guess = int(input("Make a guess: "))
        check(guess, number, 10)

elif level == "hard":
    print("You have 5 attempts to guess the number.")
    guess = 0
    while guess != number:
        guess = int(input("Make a guess: "))
        check(guess, number, 5)
        
else:
    print("Invalid input, enter 'easy' or 'hard'.")

#BUGG- not limiting to 5 and 10 guess 
