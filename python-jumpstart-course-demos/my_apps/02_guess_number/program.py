import random

print('--------------------')
print('     GUESS THAT NUMBER GAME')
print('--------------------')
print()

the_number = random.randint(0, 100)
guess = -1
try_count = 0

name = input('What is  your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    try_count += 1

    if guess > the_number:
        print('Sorry {}, your guess of {} is too too high'.format(name, guess))
    elif guess < the_number:
        print('Sorry {}, your guess of {} is too too low'.format(name, guess))
    else:
        print('Você acertou após {} tentativas'.format(try_count))
