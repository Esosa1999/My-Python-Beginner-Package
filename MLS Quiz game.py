print("Welcome to Medical laboratory science quiz game")


AI= input('Would you like to play with me? Yes/no. ')

if AI.lower()=='yes':
    print('Welcome to medical laboratory science quiz game designed by Esosa.')
else:
    quit()

AI_2=input('Are you a medical laboratory Scientist?  ')
if AI_2.lower() =='yes':  
    print('Good to have you my fellow colleague.')
    
else:
    print('This quiz game is only for a profesional medical laboratory scientist.')
    quit()

score=0


# Question 1

Question=input('What type of stain is geimsa? ')
if Question.lower() == 'romanowsky stain':
    print('correct!!')
    score=score + 1
else:
    print('wrong!!')

# Question 2

Question_2=input('Nutrient agar is a differential agar. True or False? ')
if Question_2.lower()=='true':
    print('wrong!!')
    

if Question_2.lower()=='false':
    print('correct!!')
    score=score+1


# Question 3

Question_3=input('What is the meaning of PCV? ')
if Question_3.lower()== 'packed cell volume':
    print('Correct!!')
    score=score+1
else:
    print('wrong!!')

# Question 4
    
Question_4=input('In using centrifuge, specimens must be spun________? (A). Without a cap on, (B). With a cap on, (C). Both A and B, (D). None of these. ')
if Question_4.lower()== 'b':
    print('Correct!!')
    score=score+1
else:
    print('Wrong!!')

# Question 5
    
Question_5=input('What should be used in a water bath?  (A). Tap water, (B). Boiled water, (C). Distilled water, (D). Purified water. ')
if Question_5.lower()=='d':
    print('Correct!!')
    score=score+1
else:
    print('Wrong!!') 

# Question 6

Question_6=input('A variation in Erythrocyte shape is called_______   ')
if Question_6.lower()== 'poikilocytosis':
    print('Correct!!')
    score=score+1
else:
    print('Wrong!!')

# Question 7
Question_7=input('Red blood cell count can identify one of the following? (A). Leukemia, (B). Sickle cell disease, (C). Infection, (D). Anemia  ')
if Question_7.lower()=='d':
    print('Correct!!')
    score=score+1
else:
    print('Wrong!!')

# Question 8
Question_8=input('When a blood test shows an increase in a type of white blood cells called neutrophils, it may suggest which of the following?  (A). Bacterial infection, (B). A clotting disorder, (C). Vitamin deficiency, (D). Cancer.   ')
if Question_8.lower()=='a':
    print('Correct!!')
    score=score+1
else:
    print('Wrong!!')

# Question 9
Question_9=input('Before a person can receive a blood transfusion, which of the following must be determined?  (A). Platelet count, (B). Blood type, (C). Blood glucose level, (D). Hemoglobin level.  ')
if Question_9.lower()=='b':
    print('Correct!!')
    score=score+1
else:
    print('Wrong!!')

# Question 10
Question_10=input('E.coli, is a gram-negative cocci. True or false? ')
if Question_10.lower()=='true':
    print('Wrong!!')
elif Question_10.lower()=='false':
    print('Correct!!')
    score=score+1


print('You got' , str(score) , 'questions correct!')
print('Thank you for playing with me :)')