"""
Automate the Boring Stuff with Python
Chapter 10 Debugging - Project: Debugging Coin Toss
Description:
    The following program is meant to be a simple coin toss guessing
    game. The player gets two guesses (it’s an easy game). However,
    the program has several bugs in it. Run through the program a few
    times to find the bugs that keep the program from working correctly.
"""
import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if ('tails', 'heads')[toss] == guess:
# toss == guess -> ('tails', 'heads')[toss] == guess
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input() # guesss -> guess
    if ('tails', 'heads')[toss] == guess:
       print('You got it!')
    else:
       print('Nope. You are really bad at this game.')