import os
from typing import Union
from database import location as locationDatabase
from database import facility as facilityDatabase
from database import customer as customerDatabase
from database import product as productDatabase
from database import shop as shopDatabase
from utilsFolder.text_style import TextStyle
from models.Customer import Customer
from models.Facility import Facility

from models.Shop import Shop

def sellProduct():
    while True:
        try:
            # Check IF Theres At Least 1 Customer Available
            isAvailable = False
            for c in customerDatabase:
                if not c.isCheckOut:
                    isAvailable = True
            
            if not isAvailable:
                os.system('clear||cls')
                print(f'{TextStyle.RED}No Customer Available In The Zoo{TextStyle.END}')
                input('\nPress Enter...')
                break

            n = 0
            os.system('clear||cls')
            print('0. Back')
            for l in locationDatabase:
                n += 1
                print(f'{n}. {l.name} ({l.description})')

            location = int(input('\nChoose Location: '))

            if not (0 <= location <= n):
                os.system('clear||cls')
                print(f'{TextStyle.RED}Please Input A Number Between 0 - {n}{TextStyle.END}')
                input('\nPress Enter...')
                continue

            if location == 0: break
            
            while True:
                try:
                    os.system('clear||cls')
                    print(f'Stand(s) That Placed In {locationDatabase[location-1].name}:')

                    num = 1
                    standData: list[Union[Shop, Facility]] = []

                    # Loop Facility That Has locationId = location
                    for f in facilityDatabase:
                        if f.locationId == locationDatabase[location-1]._id and len(f.productIds) != 0:
                            standData.append(f)

                    # Loop Shop That Has locationId = location
                    for s in shopDatabase:
                        if s.locationId == locationDatabase[location-1]._id:
                            standData.append(s)

                    # Means No Stand In This Location
                    if len(standData) == 0:
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}No Stand Located In This Area{TextStyle.END}')
                        input('\nPress Enter...')
                        break
                    
                    print('\n0. Exit')
                    for s in standData:
                        print(f'{num}. {s.name}')
                        num += 1

                    stand = int(input('\nChoose Stand: '))

                    if not (0 <= stand <= num-1):
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Please Input A Number Between 0 - {num-1}{TextStyle.END}')
                        input('\nPress Enter...')
                        continue

                    if stand == 0: break

                    isRp, isYen, isDollar = True, False, False

                    while True:
                        try:
                            selectedStand = standData[stand-1]
                            
                            os.system('clear||cls')
                            print('RUPIAH: Change To Rupiah Currencies')
                            print('DOLLAR: Change To Dollar Currencies')
                            print('YEN: Change To Yen Currencies')
                            print(f'\n{selectedStand.name}\'s Menu:')
                            print('0. Exit')

                            menu = selectedStand.showMenu(isRp, isYen, isDollar)

                            sell = input('\nEnter Order: ')

                            if sell.lower() == 'rupiah':
                                isRp, isYen, isDollar = True, False, False
                                continue
                            elif sell.lower() == 'dollar':
                                isRp, isYen, isDollar = False, False, True
                                continue
                            elif sell.lower() == 'yen':
                                isRp, isYen, isDollar = False, True, False
                                continue

                            sell = int(sell)

                            if sell == 0: break

                            if not (0 <= sell <= len(selectedStand.productIds)):
                                os.system('clear||cls')
                                print(f'{TextStyle.RED}Please Input A Number Between 0 - {len(selectedStand.productIds)}{TextStyle.END}')
                                input('\nPress Enter...')
                                continue
                            
                            selectedProduct = menu[sell-1]

                            if selectedProduct.stock == 0:
                                os.system('clear||cls')
                                print(f'{TextStyle.RED}Product Out Of Stock, Please Select Another Product{TextStyle.END}')
                                input('\nPress Enter...')
                                continue
                                
                            while True:
                                try:
                                    if selectedProduct.stock == 0:
                                        break

                                    customerNotCheckOut: list[Customer] = []
                                    count = 0
                                    os.system('clear||cls')
                                    print(f'Sell {selectedProduct.name} To:')
                                    print('0. Exit')
                                    for c in customerDatabase:
                                        if not c.isCheckOut:
                                            customerNotCheckOut.append(c)

                                    for c in customerNotCheckOut:
                                        print(f'{count+1}. {c.name}')
                                        count += 1

                                    customerSell = int(input(f'\nSelect Customer: '))

                                    if not(0 <= customerSell <= count):
                                        os.system('clear||cls')
                                        print(f'{TextStyle.RED}Please Input A Number Between 0 - {count}{TextStyle.END}')
                                        input('\nPress Enter...')
                                        continue

                                    if customerSell == 0:
                                        break

                                    selectedStand.sellItem(selectedProduct.price, selectedProduct._id, customerNotCheckOut[customerSell-1]._id)
                                    
                                    for p in productDatabase:
                                        if p._id == selectedProduct._id:
                                            p.stock -= 1

                                    os.system('clear||cls')
                                    print(f'{TextStyle.GREEN}Product Sold To {customerNotCheckOut[customerSell-1].name}{TextStyle.END}')
                                    input('\nPress Enter...')
                                except:
                                    os.system('clear||cls')
                                    print(f'{TextStyle.RED}Input Must Be A Number{TextStyle.END}')
                                    input('\nPress Enter...')
                        except:
                            os.system('clear||cls')
                            print(f'{TextStyle.RED}Input Must Be A Number{TextStyle.END}')
                            input('\nPress Enter...')
                except:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Input Must Be A Number{TextStyle.END}')
                    input('\nPress Enter...')
        except:
            os.system('clear||cls')
            print(f'{TextStyle.RED}Input Must Be A Number{TextStyle.END}')
            input('\nPress Enter...')
