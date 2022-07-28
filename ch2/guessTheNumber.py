# using random function for a game. Written with vim

import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

    # ask player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low..')
    elif guess > secretNumber:
        print('Your guess is too high..')
    else:
        break  # this is the correct guess

if guess == secretNumber:
    print('Good job you guesses the secret number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number is was thinking of was ' + str(secretNumber))
