from models.Customer import Customer
from database import customer as customerDatabase
from database import product as productDatabase
from database import shop as shopDatabase
from models.enums.Gender import Gender
from utilsFolder.text_style import TextStyle
import os

def customer():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Check In Customer')
        print('2. Check Out Customer')
        print('3. List Customer')

        choice = input('\nEnter Option: ')

        if choice == '0': break

        if choice == '1':
            os.system('clear||cls')
            name = input('Name: ')

            while True:
                try:
                    os.system('clear||cls')
                    age = int(input('Age: '))
                    break
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                    input('\nPress Enter...')
            
            while True:
                try:
                    os.system('clear||cls')
                    print('1. Male')
                    print('2. Female')

                    gender = int(input("\nGender : "))

                    if not (1 <= gender <= 2):
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Please Input A Number Between 1 - 2{TextStyle.END}')
                        input('\nPress Enter...')
                    else:
                        if gender == 1:
                            gender = Gender.MALE
                        else:
                            gender = Gender.FEMALE
                        break
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                    input('\nPress Enter...')
                    
            customerDatabase.append(Customer(name, age, gender))

            # Auto Buy Ticket
            for s in shopDatabase:
                if s._id == 'c61195f6-c28b-46c1-b26d-17125573a378':
                    for p in productDatabase:
                        if p._id == '8dda208f-2171-47ab-b847-d94412e7afaa':
                            s.sellItem(p.price, '8dda208f-2171-47ab-b847-d94412e7afaa', customerDatabase[-1]._id)

            os.system('clear||cls')
            print(f"{TextStyle.GREEN}{customerDatabase[-1].name} Checked In Successfully{TextStyle.END}")
            input('\nPress Enter...')
        if choice == '2':
            if len(customerDatabase) == 0: 
                os.system('clear||cls')
                print(f'{TextStyle.RED}No Customer Were Found, Please Create A New One...{TextStyle.END}')
                input('\nPress Enter...')
                break
            
            while True:
                try:
                    n = 1
                    customerThatNotCheckout: 'list[Customer]' = []

                    os.system('clear||cls')
                    print('0. Exit')
                    for c in customerDatabase:
                        if not c.isCheckOut:
                            customerThatNotCheckout.append(c)
                    if len(customerThatNotCheckout) == 0:
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}No Customer With Status Not Check Out Found{TextStyle.END}')
                        input('\nPress Enter...')
                        break

                    for c in customerThatNotCheckout:
                        print(f'{n}. {c.name}, {c.age} | {c.gender.value}')
                        n += 1

                    customer = int(input('\nChoose Customer: '))
                    if not (0 <= customer <= n-1):
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Please Input A Number Between 0 - {n-1}{TextStyle.END}")
                        input('\nPress Enter...')
                    else:
                        break
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                    input('\nPress Enter...')

            if customer == 0: break

            for c in customerDatabase:
                if c._id == customerThatNotCheckout[customer-1]._id:
                    c.isCheckOut = True

            os.system('clear||cls')
            print(f'{TextStyle.GREEN}{customerThatNotCheckout[customer-1].name} Checked Out Successfully{TextStyle.END}')
            input('\nPress Enter...')

        if choice == '3':
            if len(customerDatabase) == 0: 
                os.system('clear||cls')
                print(f'{TextStyle.GREEN}No Customer Were Found, Please Create A New One...{TextStyle.END}')
                input('\nPress Enter...')
                break
            n = 1
            os.system('clear||cls')
            for c in customerDatabase:
                if c.isCheckOut:
                    print(f'{n}. {c.name}, {c.age} | {c.gender.value} - Check Out')
                else:
                    print(f'{n}. {c.name}, {c.age} | {c.gender.value}')
                n += 1
            input('\nPress Enter...')