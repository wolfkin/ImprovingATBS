#This is a guess the number game from Automate the boring stuff with python
#

import random

continueFlag = 1
user = ""

print('Welcome to the improved number guessing game\n\n')

def nameCheck(word):
	while word != "":
		print('Hello ' + word + '. Would you like to change your name?')
		changeName = input().lower()
		if changeName[0] == 'n':
			print('Alright keep playing ' + word)
			return word
		word = input('Hello. What is your name? -->')
		return word
	word = input('Hello. What is your name? -->')
	return word

while continueFlag == 1:
	exit = ["n", "no", "exit", "end"]

	user = nameCheck(user)
	print('your name is [' + user + ']')

	if user == "debug":
		print('Debug Mode: On')
		print('\nDebug Mode: Exit is' + str(exit) + '\n\n')

	exit.append(input('What is your safeword?\n').lower())

	if user == "debug":
		print('\nDebug Mode: Exit is' + str(exit) + '\n\n')

	print('Well ' + user + ', I am thinking of a number between 1 and 20')
	secretNumber = random.randint(1,20)

	if user == "debug":
		print('>@@ Debug Mode: Secret Number is ' + str(secretNumber) + '  @@<')

	for guessCount in range(1,7):
		print('Take a guess.')
		guess = int(input())

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
	if playAgain in exit:
		continueFlag = 0
