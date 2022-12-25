from typing import Union
from database import location as locationDatabase
from database import facility as facilityDatabase
from database import customer as customerDatabase
from database import shop as shopDatabase
from database import product as productDatabase
import os
from models.Facility import Facility
from models.RupiahToDollar import RupiahToDollar
from models.RupiahToYen import RupiahToYen

from models.Shop import Shop

def sellProduct():
    while True:
        # Check IF Theres At Least 1 Customer Available
        isAvailable = False
        for c in customerDatabase:
            if not c.isCheckOut:
                isAvailable = True
        
        if not isAvailable:
            print('No Customer Available In The Zoo')
            input('Press Enter...')
            break

        os.system('clear||cls')
        print('0. Back')

        n = 0

        for l in locationDatabase:
            n += 1
            print(f'{n}. {l.name} ({l.description})')

        location = int(input('\nChoose Location: '))

        if not (0 <= location <= n):
            print(f'Please Input A Number Between 0 - {n}')
            input('Press Enter...')
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
                    print(f'No Stand Located In This Area')
                    input('Press Enter...')
                    break
                
                print('\n0. Exit')
                for s in standData:
                    print(f'{num}. {s.name}')
                    num += 1

                stand = int(input('\nChoose Stand: '))

                if not (0 <= stand <= num-1):
                    print(stand)
                    print(f'Please Input A Number Between 0 - {num-1}')
                    input('Press Enter...')
                    continue

                if stand == 0: break

                isRp, isYen, isDollar = True, False, False

                while True:
                    try:
                        os.system('clear||cls')
                        print('RUPIAH: Change To Rupiah Currencies')
                        print('DOLLAR: Change To Dollar Currencies')
                        print('YEN: Change To Yen Currencies')
                        print(f'\n{standData[stand-1].name}\'s Menu:')
                        print('0. Exit')
                        if isRp:
                            menuCount = len(standData[stand-1].productIds)
                            standData[stand-1].showMenu()
                        else:
                            menuCount = 0
                            for pId in standData[stand-1].productIds:
                                for p in productDatabase:
                                    if pId == p._id:
                                        if isYen:
                                            print(f'{menuCount+1}. {RupiahToYen(p).displayDescriptionInYen()}')
                                        elif isDollar:
                                            print(f'{menuCount+1}. {RupiahToDollar(p).displayDescriptionInDollar()}')
                                        menuCount += 1

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

                        if not (0 <= sell <= menuCount):
                            print(f'Please Input A Number Between 0 - {menuCount}')
                            input('Press Enter...')
                            continue
                        
                        count = 0               
                        os.system('clear||cls')
                        print('Customer:')
                        for c in customerDatabase:
                            if not c.isCheckOut:
                                print(f'{count+1}. {customerDatabase[count].name}')
                                count += 1

                        customerSell = int(input('\nSell To Who?: '))

                        input('Press Enter...')
                    except:
                        print("Input Must Be A Number")
                        input('Press Enter...')
            except:
                print(f'Input Must Be A Number')
                input('Press Enter...')
