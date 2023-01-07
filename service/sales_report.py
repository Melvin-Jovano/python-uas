import os
from database import sales as salesDatabase
from database import productType as productTypeDatabase
from database import product as productDatabase
from models.Product import Product, RupiahToDollar, RupiahToYen
from utilsFolder.text_style import TextStyle

def salesReport():
    isRp, isYen, isDollar = True, False, False

    while True:
        os.system('clear||cls')
        print('RUPIAH: Change To Rupiah Currencies')
        print('DOLLAR: Change To Dollar Currencies')
        print('YEN: Change To Yen Currencies')
        print('0. Exit')
        print(f'\n{TextStyle.GREEN}Total Sales: {salesDatabase.getTotalSales(isRp, isYen, isDollar)}{TextStyle.END}\n')

        num = 0
        for pt in productTypeDatabase:
            print(f'{TextStyle.BLUE}{TextStyle.BOLD}{num+1}. {pt.name}{TextStyle.END}')
            isFound = False
            subNum = 0
            for p in productDatabase:
                totalSales = 0
                if p.productTypeId == pt._id:
                    for s in salesDatabase.sales:
                        if s['productId'] == p._id:
                            totalSales += s['amount']
                    if isRp:
                        print(f'{num+1}.{subNum+1}. {p.name}, {TextStyle.GREEN}Rp.{"{:20,.2f}".format(totalSales).strip()}{TextStyle.END}')
                    elif isDollar:
                        print(f'{num+1}.{subNum+1}. {TextStyle.GREEN}{RupiahToDollar(Product(p.name, totalSales, p.stock, "")).displayDescriptionInDollar()}{TextStyle.END}')
                    elif isYen:
                        print(f'{num+1}.{subNum+1}. {TextStyle.GREEN}{RupiahToYen(Product(p.name, totalSales, p.stock, "")).displayDescriptionInYen()}{TextStyle.END}')
                    subNum += 1
                    isFound = True
            if not isFound:
                print(f'~ No Sales Found ~')
            print()
            num += 1

        currency = input('Change Currency To: ')

        if currency == '0': break

        if currency.lower() == 'rupiah':
            isRp, isYen, isDollar = True, False, False
        elif currency.lower() == 'yen':
            isRp, isYen, isDollar = False, True, False
        elif currency.lower() == 'dollar':
            isRp, isYen, isDollar = False, False, True