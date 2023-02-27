"""A number-guessing game."""

# Put your code here
import random

print('hi!')


def guessing_game():
    # throwing in a print to see if it gives us a random number
    number = random.randint(1, 100)
    print(number)
    name = input("Howdy! What's your name?")
    print(f"{name}, I'm thiniking of a number between 1 and 100 \n Try to guess my number!")

    guess = int(input("Your guess? "))
    if guess == number:
        print(f"Well done, {name}, you found my number!")
    else:
        print("That's the wrong number!")


guessing_game()
