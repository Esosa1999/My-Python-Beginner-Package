import random
import time
OPERATORS= ['+', '-', '*']
MIN_OPERAND= 3
MAX_OPERAND= 12
Total_problems=12

def generate_problems():
    Left=random.randint(MIN_OPERAND,MAX_OPERAND)
    Right=random.randint(MIN_OPERAND,MAX_OPERAND)
    symbol=random.choice(OPERATORS)
    Math_problem= str(Left) + ' ' + symbol + ' ' + str(Right)
    Answer=eval(Math_problem)
    return Math_problem, Answer


input('press enter to start')
print('-----------------')
correct_answers=0
wrong_answers=0
start_time=time.time()

for i in range(Total_problems):
   Math_problem,Answer=generate_problems()
   while True:
       guess= input('Problem' + ' ' +'#'+ str(i+1) + ':' '\n' +  Math_problem + '=' ' ')
       if guess== str(Answer):
           print('Correct!')
           correct_answers=correct_answers+1
           break
       else:
           print('Wrong!')
           wrong_answers=wrong_answers+1
           break
       

end_time=time.time()
time_spent= end_time - start_time
print('Time spent :', time_spent, 'seconds!')
print('You got', correct_answers, 'questions correctly!')
print('You got', wrong_answers, 'questions wrong!')