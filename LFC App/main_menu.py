import owner_menu
import user_menu

user = {'user':'pass',
        'owner':'pass'}      

# MENU LOGIN
def login():
    while True:
        username = input('\nLogin menu :\n=============\n\nEnter your username (enter x to cancel): ')
        if username == 'x':
            return
        else :
            userPass = input('Enter your password: ')    
            if username in user and userPass == user[username]:
                print('\n*Login Successful!*')
                print(f'\n-----------------------------------------\nHello {username}, Welcome to L Fried Chicken !\n-----------------------------------------')
                if username == 'owner' and userPass == user['owner']:
                    owner_menu.menuOwner()
                else : user_menu.menuUser()
                break
            else : print('\n*Invalid username or password. Please try again.*')

# MENU SIGNUP  
def signup():
    while True:
        newUser = input('\nSignUp Menu\n=============\n\nUsername and password must be alphabet more than 4 char\nEnter your username (enter x to cancel): ')
        if newUser == 'x':
            return
        elif len(newUser) <= 4 :
            print('\n*Invalid input!*')
        elif newUser in user:
            print('\n*Username already exist!*')
        else :
            newPass = input('Enter your password : ')
            if len(newPass) <= 4 :
                print('\n*Invalid input!*')
            else :
                user[newUser]=newPass
                print('\n*New user added!*')
                break

# ENTER YOUR USERNAME AND PASSWORD
while True:
    try :
        userInp = int(input('\n------------------------------\nWelcome to L Fried Chicken App\n------------------------------\n\n1. SignUp\n2. Login\n3. Exit App\nChoose menu number : '))
    except :
        print('\n*Invalid input!*')
        continue
    # MENU SIGNUP
    if userInp == 1:    
        signup()
    # MENU LOGIN
    elif userInp == 2:
        login()
    # MENU EXIT APP
    elif userInp == 3:
        print('\n*Thank you for using this app!*\n')
        exit()
    else:
        print('\n*Invalid input!*')