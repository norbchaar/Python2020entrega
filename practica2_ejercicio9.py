# This is a Guess the Number game.
import random

def hint(guess, number, guesses_taken):
    if guess != number and guesses_taken == 3:
        if number % 2 == 0:
            print('Hint: The number is even.')
        else:
            print('Hint: The number is odd.')	

guesses_taken = 0
print('Hello! What is your name?')
my_name = input()
 
number = random.randint(1, 51)
print('Well, ' + my_name + ', I am thinking of a number between 1 and 50.')

guessing = True
while guessing:
    guesses_taken+= 1 
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')
        
    hint(guess, number, guesses_taken)
	
    if guess == number:
        guessing = False

guesses_taken = str(guesses_taken)

print('Good job, ' + my_name + '! You guessed my number in ' +
	guesses_taken + ' guesses!')
