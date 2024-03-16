import random

# Assume a minimum of two and a maximum of four persons will be playing this game.

def dice_roller():
    Dice=6
    random_number=random.randint(1,Dice)
    return random_number

while True:
 Number_of_users=input('Enter the number of players (2-4): ')
 if Number_of_users.isdigit():
     users= int(Number_of_users)
 if 2<=users<=4:
     print('game on')
     break
 else:
     print('invalid')
     print('please input a value between (2-4)')
     continue
 

max_score=50
player_scores= [0 for _ in range(users)]

while max(player_scores) < max_score:  
    for player_idx in range(users):
        print('\nplayer number', player_idx + 1, 'turn has just started!')
        print('Your total score is:', player_scores[player_idx], '\n')
        current_score=0
        while True:
            should_roll=input('Would you like to roll? (YES/NO)')
            if should_roll.lower()!='yes':
                quit()
            value=dice_roller()
            if value==1:
                print('You rolled a 1!, Turn done!')
                current_score=0
                break
            else:
                current_score=current_score+value
                print('You rolled a:' , value)
                
            
            print('Your score is:' , current_score)
        player_scores[player_idx]== player_scores[player_idx] + current_score
        print('Your total score is:' , player_scores[player_idx])
                

max_score=max(player_scores)
winning_idx=player_scores.index(max_score)
print('player number', winning_idx + 1, 'is the winner with a score of:', max_score)
 


        
