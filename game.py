"""A number-guessing game."""

# Put your code here
import random

print('hi!')


def guessing_game():
    # throwing in a print to see if it gives us a random number
    counter = 1
    number = random.randint(1, 100)
    name = input("Howdy! What's your name?")
    print(f"{name}, I'm thiniking of a number between 1 and 100 \n Try to guess my number!")

    guess = int(input("Your guess? "))
    while guess != number:
        if guess > number:
            print("Your guess is too high, try again!")
        else:
            print("Your guess is too low, try again!")
        guess = int(input("Your guess? "))
        counter += 1
    print(f"Well done! You found my number in {counter} tries :)")


guessing_game()
