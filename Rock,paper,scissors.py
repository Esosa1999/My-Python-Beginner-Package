import random

User_wins = 0
Computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type rock/paper/scissors or Q to Quit: ').lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print('Computer picked', computer_pick)

    if user_input == 'rock' and computer_pick == 'scissors':
        print('rock destroys scissors!')
        print('You win!!!')
        User_wins += 1
        continue
    if user_input == 'rock' and computer_pick == 'paper':
        print('paper covers rock!!')
        print('You lose!!')
        Computer_wins += 1
        continue

    if user_input == 'paper' and computer_pick == 'scissors':
        print('scissors cuts paper!')
        print('You lose!!')
        Computer_wins += 1
        continue
    if user_input == 'paper' and computer_pick == 'rock':
        print('paper covers rock!!')
        print('You win!!')
        User_wins += 1
        continue

    if user_input == 'scissors' and computer_pick == 'paper':
        print('scissors cuts paper!!')
        print('You win!!')
        User_wins += 1
        continue
    if user_input == 'scissors' and computer_pick == 'rock':
        print('rock destroys scissors!!')
        print('You lose!!')
        Computer_wins += 1
        continue

    if user_input == computer_pick:
        print("It's a tie!")

# After the loop ends, print the final results
print(f'You won {User_wins} times.')
print(f'Computer won {Computer_wins} times.')
print('The end!')