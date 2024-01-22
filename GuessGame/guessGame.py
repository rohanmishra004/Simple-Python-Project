#Guess game - using import random library

import random

compChoice = int(random.randrange(1,10))
tries = 3


def guessGame(tries):
    UserInput = int(input('Guess a number:  '))

    if UserInput == compChoice:
        print(f'Correct Number is {compChoice}')
    elif (UserInput!=compChoice):
        print('Incorrect Number')
        tries-=1
        if tries>=1:
            guessGame(tries)
        else:
            print('All tries ended , you Fail')

guessGame(tries)

