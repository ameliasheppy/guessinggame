"""A number-guessing game."""

# Put your code here
import random

print('hi!')

#
name = input("Howdy! What's your name?")
print(f"{name}, I'm thinking of a number between 1 and 100 \n Try to guess my number!")


def guessing_game():
    # throwing in a print to see if it gives us a random number
    counter = 0
    number = random.randint(1, 100)
    print(number)
    guess = 'cats'
    max_count = 3

    while guess != number and counter <= max_count:
        try:
            guess = int(input("Your guess? "))
        except ValueError:
            print('Please enter a valid number')
            continue
        if guess < 101 and guess > 0:
            if guess > number:
                print("Your guess is too high, try again!")
            else:
                print("Your guess is too low, try again!")
        else:
            print('Sorry, you need to give a number from 1-100!')
        counter += 1

    if guess == number:
        print(f"Well done! You found my number in {counter} tries :)")
    else:
        print('OOPS! You exceeded the max number of attemped guesses, please start over.')
    return counter


scores = []
scores.append(guessing_game())

print(scores)
