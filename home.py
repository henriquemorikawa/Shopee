import sys
from getpass import getpass
from actions import add_sale, output_all_sales, output_sales_ranking, edit_item, sales_list

login = False
check_username = "shopee"
check_password = "check"

#login page
def home_page():
    attempts = 0
    print('\n\n\n\n\n\nWelcome to the Seller Page!\n\n\n\n\n\n')
    while True: 
        
        username = input("Username: ")
        password = getpass("Password: ")

        if attempts >= 2:
            sys.exit("\nToo many failed attempts. Try again later :(\n")

        if username == check_username:
            if password == check_password:
                print('\nWelcome back ' + username + ' :)')
                login = True  
                menu(login)
                break
                
            else:
                print("\nInvalid Username/Password\n")
                attempts += 1
        else:
            print("\nInvalid Username/Password\n")
            attempts += 1  

#main menu page
def menu(login):
    if(login):
        while True:
            options = ['1', '2', '3', '4']
            action = input('\nWhat would you like to do? (type a number)\n\n 1. Register a Sale\n 2. Check Sales\n 3. Edit/Remove Sale\n 4. Exit\n\n ')

            if action not in options:
                print('\nPlease type one of the numbers.\nYour input was: ' +  action)
            else:
                next_step(action)
                break

#action based on user input
def next_step(action):
    if action == '1':
        index = ''
        while True:
            add_sale(index)
            login = True
            menu(login)

    elif action == '2':
        output_all_sales(sales_list)
        output_sales_ranking(sales_list)
        login = True
        menu(login)

    elif action == '3':
        edit_item(sales_list)
        login = True
        menu(login)
    
    else:
        login = False
        home_page()

home_page()