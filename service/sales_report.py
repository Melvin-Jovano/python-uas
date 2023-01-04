import os
from database import sales as salesDatabase
from database import productType as productTypeDatabase
from database import product as productDatabase
from models.Product import Product, RupiahToDollar, RupiahToYen

def salesReport():
    isRp, isYen, isDollar = True, False, False

    while True:
        os.system('clear||cls')
        print('RUPIAH: Change To Rupiah Currencies')
        print('DOLLAR: Change To Dollar Currencies')
        print('YEN: Change To Yen Currencies')
        print('0. Exit')
        print(f'\nTotal Sales: {salesDatabase.getTotalSales(isRp, isYen, isDollar)}\n')

        num = 0
        for pt in productTypeDatabase:
            print(f'{num+1}. {pt.name}')

            subNum = 0
            for p in productDatabase:
                totalSales = 0
                if p.productTypeId == pt._id:
                    for s in salesDatabase.sales:
                        if s['productId'] == p._id:
                            totalSales += s['amount']
                    if isRp:
                        print(f'{num+1}.{subNum+1}. {p.name}, Rp.{"{:20,.2f}".format(totalSales).strip()}')
                    elif isDollar:
                        print(f'{num+1}.{subNum+1}. {RupiahToDollar(Product(p.name, totalSales, p.stock, "")).displayDescriptionInDollar()}')
                    elif isYen:
                        print(f'{num+1}.{subNum+1}. {RupiahToYen(Product(p.name, totalSales, p.stock, "")).displayDescriptionInYen()}')
                    subNum += 1
            print()
            num += 1

        currency = input('\nChange Currency To: ')

        if currency == '0': break

        if currency.lower() == 'rupiah':
            isRp, isYen, isDollar = True, False, False
        elif currency.lower() == 'yen':
            isRp, isYen, isDollar = False, True, False
        elif currency.lower() == 'dollar':
            isRp, isYen, isDollar = False, False, True