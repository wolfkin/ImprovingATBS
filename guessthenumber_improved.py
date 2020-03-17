#This is a guess the number game
import random

continueFlag = 1
user = "red"

print('Welcome to the improved number guessing game\n\n')

def nameCheck(word):
	if word != "":
		print('Hello ' + word + '. Would you like to change your name?')
		changeName = str(input().lower)
		print('Change ==> ' + changeName)
		changeName = changeName[1]
		print('Change 1st letter ==> ' + changeName)
		if changeName == 'n':
			print('Alright keep playing ' + word)
	word = input('Hello. What is your name? -->')
	print('your name is ' + word)
	return word

while continueFlag == 1:
	exit = ["n", "no", "exit", "end"]

	user = nameCheck(user)
	print('your name is [' + user + ']')

	if user == "debug":
		print('Debug Mode: On')
		print('\nDebug Mode: Exit is' + str(exit) + '\n\n')

	exit.append(input('What is your safeword?\n'))

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
	playAgain=input().lower
	if playAgain in exit:
		continueFlag = 0
