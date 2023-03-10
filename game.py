"""A number-guessing game."""

# Put your code here
from random import randint

def choose_mode():
    name = input("Howdy! What's your name?")
    choice = input(f"A if you want to guess the computer's number, or B if you want the computer to guess yours: ").lower()
    if choice == 'a':
        play_multiple_rounds()
    else:
        play_against_computer()

def guessing_game(min, max):
    # throwing in a print to see if it gives us a random number
    counter = 0
    number = randint(min, max)
    print(number)
    guess = 'cats'
    max_count = 3

    while guess != number and counter <= max_count:
        try:
            guess = int(input("Your guess? "))
        except ValueError:
            print('Please enter a valid number')
            continue
        if guess < max+1 and guess > min-1:
            if guess > number:
                print("Your guess is too high, try again!")
            else:
                print("Your guess is too low, try again!")
        else:
            print(f'Sorry, you need to give a number from {min}-{max}!')
        counter += 1

    if guess == number:
        print(f"Well done! You found my number in {counter} tries :)")
    else:
        print('OOPS! You exceeded the max number of attemped guesses, please start over.')
    return counter

def play_multiple_rounds():
    scores = [10] 
    wantCont = 'y'
    while wantCont.lower() in ('yes','y'):
        lowRange = int(input("Enter start number for this round"))
        highRange = int(input("Enter end number for this round"))
        while(highRange<lowRange):
            highRange = int(input(f"Put a number higher than {lowRange}, please: "))
        scores.append(guessing_game(lowRange, highRange))
        print(scores)
        if scores[-1] == min(scores[:-1]):
            print(f"You tied the best score")
        elif scores[-1] < min(scores[:-1]):
            print(f"NICE! New high score of {scores[-1]}")
        else:
            print(f"You didn't beat the best score, which is {min(scores)}. Sorry")
        wantCont = input("Do you want to play another round? Yes/no :")
    print(f"The best score was {min(scores)}. Bye! Thanks for playing!")

#Bianca had the excellent idea to use a binary search method to use on the guesses by the computer
def play_against_computer():
    print("We'll guess your number!")
    lowRange = int(input("What's the lowest the number could be? "))
    highRange = int(input("what's the highest the number could be ?"))
    feedback = 'n'
    guess = ((highRange - lowRange) // 2) + lowRange
    while feedback != 'correct':
        if feedback == 'too high':
            highRange = guess
        elif feedback == 'too low':
            lowRange = guess
        else:
            print("I don't understand")
        guess = ((highRange - lowRange) // 2) + lowRange
        print(f"My guess is {guess}")
        feedback = input("Too high/ Too low/ correct ?: ").lower()
    print("I got it!")

choose_mode()