import os
from database import sales as salesDatabase

def salesReport():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Overall Sales')

        choice = input('Enter Option: ')

        if choice == '0': break

        isRp, isYen, isDollar = True, False, False

        if choice == '1':
            while True:
                os.system('clear||cls')
                print('RUPIAH: Change To Rupiah Currencies')
                print('DOLLAR: Change To Dollar Currencies')
                print('YEN: Change To Yen Currencies')
                print('0. Exit')
                print(f'\nTotal Sales: {salesDatabase.getTotalSales(isRp, isYen, isDollar)}')

                currency = input('Change Currency To: ')

                if currency == '0': break

                if currency.lower() == 'rupiah':
                    isRp, isYen, isDollar = True, False, False
                elif currency.lower() == 'yen':
                    isRp, isYen, isDollar = False, True, False
                elif currency.lower() == 'dollar':
                    isRp, isYen, isDollar = False, False, True