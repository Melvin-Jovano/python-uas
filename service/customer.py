from models.Customer import Customer
from database import customer as customerDatabase
from models.enums.Gender import Gender
import os

def customer():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Check In Customer')
        print('2. Check Out Customer')
        print('3. List Customer')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            os.system('clear||cls')

            name = input('Name: ')

            while True:
                try:
                    age = int(input('Age: '))
                    break
                except:
                    print("Input Must Be a Number")
                    input('Press Enter...')
            
            while True:
                try:
                    os.system('clear||cls')
                    print('1. Male')
                    print('2. Female')

                    gender = int(input("Gender : "))

                    if not (1 <= gender <= 2):
                        print('Please Input A Number Between 1 - 2')
                        input('Press Enter...')
                    else:
                        if gender == 1:
                            gender = Gender.MALE
                        else:
                            gender = Gender.FEMALE
                        break
                except:
                    print("Input Must Be a Number")
                    input('Press Enter...')
                    
            customerDatabase.append(Customer(name, age, gender))

        if choice == '2':
            os.system('clear||cls')
            if len(customerDatabase) == 0: 
                print('No Customer Were Found, Please Create A New One...')
                input('Press Enter...')
                break
            
            while True:
                try:
                    n = 1
                    customerThatNotCheckout = []

                    print('0. Exit')
                    for c in customerDatabase:
                        if not c.isCheckOut:
                            customerThatNotCheckout.append(c)
                    
                    if len(customerThatNotCheckout) == 0:
                        print('No Customer With Status Not Check Out Found')
                        input('\nPress Enter...')
                        break

                    for c in customerThatNotCheckout:
                        print(f'{n}. {c.name}, {c.age} | {c.gender.value}')
                        n += 1

                    customer = int(input('\nChoose Customer: '))
                    if not (0 <= customer <= n-1):
                        print(f'Please Input A Number Between 0 - {n-1}')
                    else:
                        break
                except:
                    print("Input Must Be a Number")

            if customer == 0: break

            customerDatabase[customer-1].isCheckOut = True
            print('Status Has Been Updated Successfully')
            input('\nPress Enter...')

        if choice == '3':
            os.system('clear||cls')
            if len(customerDatabase) == 0: 
                print('No Customer Were Found, Please Create A New One...')
                input('Press Enter...')
                break
            
            n = 1

            for c in customerDatabase:
                print(f'{n}. {c.name}, {c.age} | {c.gender.value}', end='')
                if c.isCheckOut:
                    print(' - Check Out')
                n += 1
            input('\nPress Enter...')