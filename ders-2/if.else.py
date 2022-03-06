
username = 'samiyagmur92@gmail.com'
password = '1433255'

id = input('Pls enter your username: ')
pswrd= input('Pls enter your password: ')

while True:
   
    if (username == id) and (password == pswrd):

        print('Welcome')

        exit();
    else:
        if (username != id):
            print('You entered the wrong username')
            id = input('Pls enter your username: ')
        else:
            print('You entered the wrong password')
            pswrd= input('Pls enter your password: ')
    
