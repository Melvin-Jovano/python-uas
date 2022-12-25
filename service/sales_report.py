import os

def salesReport():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Overall Sales')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            print(f'Total Sales: ')
            input('Press Enter...')
