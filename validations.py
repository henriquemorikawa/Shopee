import datetime

#string fields validation
def get_valid_value(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please type the value in numbers")
            continue

        if value < 0:
            print("Please type a positive number")
            continue
        else:
            break

    return value

#price validation
def get_non_empty_value(prompt):
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print("Please type a valid value")
            continue

        if value and value.strip():
            break
        else:
            print('This is a mandatory field')

    return value

#date validation
def get_date(prompt):
    format = "%Y-%m-%d"
    while True:
        try:
            value = datetime.datetime.strptime(input(prompt), format)
            return value.date()

        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            continue

    
#confirm validation
def get_confirmation(prompt):
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print('\nPlease type "Y" for yes or "N" for no')
            continue

        if value and value.strip() and (value.upper() == 'Y' or value.upper() == 'N'):
            break
        else:
            print('Please type "Y" for yes or "N" for no')

    return value

#confirm item number
def get_item(prompt, list):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Please type a number')
            continue
        
        if value > len(list) or value < 0:
            print('Please enter a valid number of id')
        else:
            break

    return value