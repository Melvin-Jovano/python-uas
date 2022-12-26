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
            # TODO Group By Currencies
            print(f'Total Sales: {sum([item["amount"] for item in salesDatabase.sales])}')
            input('Press Enter...')
