import os
from database import sales as salesDatabase

def salesReport():
    isRp, isYen, isDollar = True, False, False

    while True:
        os.system('clear||cls')
        print('RUPIAH: Change To Rupiah Currencies')
        print('DOLLAR: Change To Dollar Currencies')
        print('YEN: Change To Yen Currencies')
        print('0. Exit')
        print(f'\nTotal Sales: {salesDatabase.getTotalSales(isRp, isYen, isDollar)}')

        currency = input('\nChange Currency To: ')

        if currency == '0': break

        if currency.lower() == 'rupiah':
            isRp, isYen, isDollar = True, False, False
        elif currency.lower() == 'yen':
            isRp, isYen, isDollar = False, True, False
        elif currency.lower() == 'dollar':
            isRp, isYen, isDollar = False, False, True