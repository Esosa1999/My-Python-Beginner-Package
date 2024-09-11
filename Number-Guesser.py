import random

# Get the top of range
while True:
    top_of_range = input('Type a number for the range: ')
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range > 0:
            break
        else:
            print('Please type a number greater than 0.')
    else:
        print('That is not a valid number. Try again.')

# Generate random number
random_number = random.randint(0, top_of_range)
print('I have a number in mind :)')

guesses = 0
wrong_guesses = 0

# Start guessing loop
while True:
    user_guess = input('Make a guess: ')
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
    else:
        print('Please type a valid number.')
        continue

    # Check if the guess is correct
    if user_guess == random_number:
        print(f'You got it! The number was {user_guess}.')
        break
    else:
        print('Oops! Try again.')
        wrong_guesses += 1

# Final statistics
print(f'You made {guesses} guesses.')
print(f'And you got {wrong_guesses} wrong.')