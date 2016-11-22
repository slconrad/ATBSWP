# Guess the number game!
import random

print('Hello, get ready to play - but first, what shall I call you?')
name = input()

print('Ok, ' + name + ', I am thinking of a number in between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Go ahead - take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('That guess was too low.')
    elif guess > secretNumber:
        print('That guess was too high.')
    else:
        break  # Guess the number correct and print to console

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' +
          str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' +
          str(secretNumber) + ' Too bad!')