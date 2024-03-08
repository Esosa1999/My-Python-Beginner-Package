import random

top_of_range=input('Type a number:')
if top_of_range.isdigit():
 top_of_range=int(top_of_range)
 
if top_of_range <=0:  
    print('please type in a number greater than 0')
    quit()

random_number=random.randint(0,top_of_range)
print('i have a number in mind :)')

guesses=0
wrong_guesses=0

while True:
   user_guess=input('Make a guess? ')
   if user_guess.isdigit():
      user_guess=int(user_guess)
      guesses=guesses+1
      
   else:
      print('please type in a digit :(')
      continue

   if user_guess==random_number:
    print(user_guess)
    print('You got it!')
    break
   else:
    print('oops! try again.') 
    wrong_guesses= wrong_guesses+1

print('You made', str(guesses) , 'guesses') 
print('And you got' , str(wrong_guesses) , 'wrong!')  