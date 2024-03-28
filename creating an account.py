import string
import random

#Function to generate password
def password_gen():
    character=string.ascii_letters
    digits=string.digits
    symbol=string.punctuation
    generated_password=''
    letter=True
    numbers=True
    special=True
    length=10

    if letter:
     generated_password= generated_password+character
    if numbers:
     generated_password=generated_password+digits
    if special:
     generated_password=generated_password+symbol
    
    password=''.join(random.sample(generated_password,length))
    print(password)
    return password


#Function to test password criteria

def password_criteria():
 u,l,d,s=0,0,0,0
 Uppercase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 Lowercase_letters=Uppercase_letters.lower()
 digits='12345678910'
 symbols='~!@#$%^&*()_-++[{||]}'

 while True:
    passw=input('please input a password. ')
    if (len(passw)>=10):
        for i in passw:
            if i in Uppercase_letters:
                u=u+1
            if i in Lowercase_letters:
                l=l+1
            if i in digits:
                d=d+1
            if i in symbols:
                s=s+1
    if (u>=1 and l>=1 and d>=1 and s>=1 and u+l+d+s==len(passw)):
        print('valid password')
        break
    else:
        print('Invalid password')
    
 return passw
        
# Creating an account with a Username and password
user=input('Please input your username. ')
pwd=input('please input a password that contains uppercase letters \nLowercase letters \nDigits \nSymbols \nor we generate a password for you. (generate/input)? ').lower()
if pwd=='generate':
    pwd=password_gen()
elif pwd=='input':
    pwd=password_criteria()

    
# Code to save username and password   
remember=input('Would you like us to save your username and password on your phone.(Y/N) ').lower()
while True:
    if remember=='y':
     with open('password.txt', 'a') as w:
        w.write(user + '|'+ pwd + '\n')
        print('Details saved')
        break

    elif remember=='n':
        print('Details not saved')
        break
    else:
        print('please select a valid response.(Y/N)')
        break

     





