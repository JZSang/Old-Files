import time
from random import randint
this = "y"
while this == "y":
    roll = raw_input("Would you like to roll the six-sided die? (y/n) ")
    if roll == "y":
        print("Rolling die..")
        time.sleep(2)
        print(randint(1,6))
    else:
        print("Alright")
    this = raw_input("Would you like to roll again? (y/n) ")
    if this == "n":
        print("Application Terminated")
