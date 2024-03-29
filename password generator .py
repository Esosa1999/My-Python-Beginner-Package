import random

Uppercase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Lowercase_letters=Uppercase_letters.lower()
digits='12345678910'
symbols='~!@#$%^&*()_-++[{||]}'
upper,lower,numb,symb= True, True, True, True

all=''

if upper:
    all= all+Uppercase_letters
if lower:
    all=all+Lowercase_letters
if numb:
    all=all+digits
if symb:
    all=all+symbols
length=20
amount=10

for x in range(amount):
    passwords=''.join(random.sample(all,length))
    print(passwords)

 


