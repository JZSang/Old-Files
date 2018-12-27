#System generates number
#Person guesses the number, knowing it is between 1-9
#System will tell the person if it is higher or lower
#system will confirm that it is the right number
#Return back to the start
import time
from random import randint
def incorrect(this):
    if this.isalpha() or '.' in this:
        return this
    else:
        return int(this)


print("Welcome to Guess the Number!")


decision = raw_input("Would you like to play the game (y/n)? ")
while decision == "y":
    print("The system is now generating a number..")
    time.sleep(1)
    true_number = randint(1, 9)
    print("The system has now generated a number.")
    guess = raw_input("What number do you guess (between and including 1-9)? ")
    guess_int = incorrect(guess)

    while guess_int != true_number:
        if guess_int > true_number and guess_int >= 1 and guess_int <= 9:
            print("The number is lower")
            guess = raw_input("Enter another number between 1-9! ")
        elif guess_int < true_number and guess_int >= 1 and guess_int <= 9:
            print("The number is higher")
            guess = raw_input("Enter another number between 1-9! ")
        guess_int = incorrect(guess)
        while guess_int > 9 or guess_int < 1 or guess.isalpha() or '.' in guess:
            print("That's not a number between 1 and 9!")
            guess = raw_input("Enter another number between 1-9! ")
            guess_int = incorrect(guess)
        guess_int = int(guess)
    if guess_int == true_number:
        print("Yup! %s is the number!") % (true_number)
        time.sleep(1)
        decision = raw_input("Would you like to play again (y/n)? ")
print("Application terminated")






