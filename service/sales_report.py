import os
from database import sales as salesDatabase

def salesReport():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Overall Sales')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            os.system('clear||cls')
            print('RUPIAH: Change To Rupiah Currencies')
            print('DOLLAR: Change To Dollar Currencies')
            print('YEN: Change To Yen Currencies')
            print(f'\nTotal Sales: Rp.{sum([item["amount"] for item in salesDatabase.sales])}')
            input('\nPress Enter...')
