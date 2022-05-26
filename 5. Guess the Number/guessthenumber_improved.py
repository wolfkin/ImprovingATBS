#This is a guess the number game from Automate the boring stuff with python

import random

continueFlag = 1
user = ""
low = int(1)
high = int(20)

print('Welcome to the improved number guessing game\n\n')

def nameCheck(word):
    while word != "":
        print('Hello ' + word + '. Would you like to change your name?')
        changeName = input().lower()
        if changeName[0] == 'n':
            print('Alright keep playing %s' % (word))
            return word
        word = input('Hello. What is your name? -->')
        return word
    word = input('Hello. What is your name? -->')
    return word

def debug_settings():
    global low, high
    print('Entering Debug Mode')
    print(' ___        _           __ _ ')
    print('|   \  ___ | |__  _  _ / _` |')
    print('| |) |/ -_)|  _ \| || |\__. |')
    print('|___/ \___||____/ \_._||___/ ')
    print('Debug Mode: On')
    print('\nDebug Mode: Exit is ' + str(exitValues) + '<<<\n\n')
    high  =change_number(high,"High")
    low   =change_number(low,"Low")
    
def change_number(number, kind):
        print('%s is currently %s' % (kind, str(number)))
        print('Would you like to change it? [Y]es or [N]o')
        change = input().lower()
        if change[0] != "y":
                print('%s number remains %s' % (kind,str(number)))
        else:
                print('Change %s from %s to:' % (kind,str(number)))
                number = int(input())
                print('New number is  %s' % (str(number)))
        return number


while continueFlag == 1:

    exitValues = ["n", "no", "exit", "end"]

    user = nameCheck(user)
    print('your name is [%s]' % (user))

    if user == "debug":
        debug_settings()

    exitValues.append(input('What is your safeword?\n').lower())

    if user == "debug":
        print('\nDebug Mode: Exit is %s \n\n' % (str(exitValues)))

    print('Well %s, I am thinking of a number between %s and %s' % (user, str(low), str(high)))
    secretNumber = random.randint(low,high)

    if user == "debug":
        print('>@@ Debug Mode: Secret Number is %s @@<' % (str(secretNumber)))

    for guessCount in range(1,7):
        print('Take a guess.')
        guess = int(input())   #Need to sanitize this input in case someone puts in words

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break

    if guess == secretNumber:
        print('Good job, ' + user + '! You guessed my number in ' + str(guessCount) + ' guesses!')
    else:
        print('Nope. the number I was thinking of was ' + str(secretNumber))
    print('Would you like to play again? Enter (n) to exit or your safeword.')
    playAgain=input().lower()
    if playAgain in exitValues:
        continueFlag = 0
