#A person puts in a letter
#The system certifies that it is a letter before proceeding
#The system checks if it part of the randomly generated word
#the system can say at this point that it is part of the word
#The system can say it is not part of the word. It will then limit the number of guesses by 1.
#The number of guesses max out at 5.

import random
import time

words = ['state', 'problem', 'anime', 'world', 'powerful', 'hello']

print("Welcome to Hangman!")

decision = raw_input("Would you like to play? (y/n) ")

while decision == 'y':
    print("The system is currently choosing a word.. ")
    time.sleep(0.5)
    chosen_word = random.choice(words)
    list_chosen_word = list(chosen_word)
    print("The system has chosen a word. It is %01d letters long ") % (len(chosen_word))
    underlines = "_" * len(chosen_word)
    listed_underlines = list(underlines)
    print listed_underlines
    NuLives = 5
    used_letters = []

    while "_" in listed_underlines:

        letter = raw_input("""
Choose a letter (or word!). You currently have """ + (str(NuLives)) +  " lives. ")
        worded = letter
        if letter in list_chosen_word and letter not in listed_underlines:
            indices = [i for i, x in enumerate(list_chosen_word) if x == letter]
            for numbers1 in indices:
                listed_underlines.insert(numbers1, letter)
                numbers1 += 1
                del listed_underlines[numbers1]
            print("""
            
Yup! %s is correct

""") % (letter)
        elif list(worded) == list_chosen_word:
            print (list_chosen_word)
            break
        elif letter.isalpha() or letter in listed_underlines:
            print("""
            
That's the wrong letter/word!

""")
            NuLives -= 1
        else:
            print("""
            
Invalid Answer

""")
        used_letters.extend(letter)
        print listed_underlines
        print "These are the letters you've used so far: ", used_letters

        if NuLives == 0:
            break
    if NuLives == 0:
        print("""
        
You lost! :( Looks like he's dead..""")

    elif NuLives >= 1:
        print("""
        
You won! Congratulations, you've saved the near-hanged man!

""")

    decision = raw_input("Would you like to play again? (y/n) ")










