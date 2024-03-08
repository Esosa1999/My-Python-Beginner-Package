from cryptography.fernet import Fernet

'''def write_key():
 key= Fernet.generate_key()
 with open('key.txt' , 'wb') as f:
   f.write(key)'''


def load_key():
  with open('key.txt', 'rb') as r:
    Read= r.read()
    return Read


Master_pwd=input('What is the master password? ').lower()
if Master_pwd=='esosa':
 key= load_key() + Master_pwd.encode()
 fer= Fernet(key)
 print('Alright')
else:
 print('Wrong Master Password')
 quit()


def view():
  with open('passwords.txt', 'r') as f:
     for line in f.readlines(): 
       line.rstrip()
       data=line.rstrip() 
       user , passwd= data.split('|') 
       print('Username:', user, '| password:' , 
            fer.decrypt(passwd.encode()).decode())
               
  
def add():
    name = input('Account Name: ')
    pwd = input("Password: ").encode()

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd).decode()+ "\n") 

while True:
   mode=input('Would you like to add a new password or view existing ones? (Add,View), press q to quit. ').lower()
   if mode=='q':
    break
  
   if mode == 'view':
    view()
   elif mode== 'add':
    add()
   else:
    print('invalid mode')
    continue
