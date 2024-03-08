import random

User_wins=0
Computer_wins=0

options=['rock', 'paper', 'scissors']


while True:
    user_input=input('Type rock/paper/scissors or Q to Quit: ').lower()
    if user_input.lower()== 'q':
        break
    if user_input not in options:
        continue
     
    random_number=random.randint(0,2)
    #rock=0, paper=1, scissors:2
    computer_pick=options[random_number]
    print('computer picked' , computer_pick)
    
    if user_input=='rock' and computer_pick=='scissors':
        print('rock destroys scissors!')
        print('You win!!!')
        User_wins=User_wins + 1
        continue
    if user_input=='rock' and computer_pick=='paper':
        print ('paper covers rock!!')
        print('you lose!!') 
        Computer_wins= Computer_wins + 1
        continue
   
    if user_input=='paper' and computer_pick=='scissors':
        print('scissors cuts paper!')
        print('you lose!!')
        Computer_wins= Computer_wins +  1
        continue
    if user_input=='paper'  and computer_pick=='rock':
         print ('paper covers rock!!')
         print ('you win!!')
         User_wins= User_wins + 1
         continue
    

    if user_input=='scissors' and computer_pick=='paper':
        print('scissors cuts paper!!')
        print('you win!!')
        User_wins= User_wins + 1
        continue
    if user_input=='scissors' and computer_pick=='rock':
        print('rock destroys scissors!!')
        print('you lose!!')
        Computer_wins= Computer_wins + 1
        continue
    else:
        if user_input==computer_pick:
         print('You won' , str(User_wins) , 'times.')
        print('Computer won', str(Computer_wins) , 'times.')
        print('The end!')
        break
   
