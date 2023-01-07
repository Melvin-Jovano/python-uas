from database import decorations as decorationsDatabase
from database import decoration as decorationDatabase
from database import location as locationDatabase
from database import sales as salesDatabase
from utilsFolder.text_style import TextStyle
import os
from models.Decoration import Decoration
from models.Location import Location
from models.Product import Product, RupiahToDollar, RupiahToYen

def decoration():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Decoration')
        print('2. Edit Decoration')
        print('3. Delete Decoration')

        choice = input('\nEnter Option: ')

        if choice == '0': break

        if choice == '1':
            isRp, isYen, isDollar = True, False, False

            while True:
                os.system('clear||cls')
                print('RUPIAH: Change To Rupiah Currencies')
                print('DOLLAR: Change To Dollar Currencies')
                print('YEN: Change To Yen Currencies')

                if isRp:
                    print(f'{TextStyle.GREEN}Balance, Rp.{"{:20,.2f}".format(salesDatabase.balance).strip()}{TextStyle.END}')
                elif isDollar:
                    print(f'{RupiahToDollar(Product("Balance", salesDatabase.balance, 1, "")).displayDescriptionInDollar()}')
                elif isYen:
                    print(f'{RupiahToYen(Product("Balance", salesDatabase.balance, 1, "")).displayDescriptionInYen()}')
                    
                print('\n0. Exit')

                for x, d in enumerate(decorationsDatabase):
                    if isRp:
                        print(f'{x+1}. {d["name"]}, Rp.{"{:20,.2f}".format(d["price"]).strip()}')
                    elif isDollar:
                        print(f'{x+1}. {RupiahToDollar(Product(d["name"], d["price"], 1, "")).displayDescriptionInDollar()}')
                    elif isYen:
                        print(f'{x+1}. {RupiahToYen(Product(d["name"], d["price"], 1, "")).displayDescriptionInYen()}')
                    
                decoration = input('\nSelect A Decoration To Buy: ')

                if decoration.lower() == 'rupiah':
                    isRp, isYen, isDollar = True, False, False
                elif decoration.lower() == 'yen':
                    isRp, isYen, isDollar = False, True, False
                elif decoration.lower() == 'dollar':
                    isRp, isYen, isDollar = False, False, True
                else:
                    try:
                        decoration = int(decoration)
                        if not(0 <= decoration <= len(decorationsDatabase)):
                            os.system('clear||cls')
                            print(f'{TextStyle.RED}Please Input A Number Between 0 - {len(decorationsDatabase)}{TextStyle.END}')
                            input('\nPress Enter...')
                            continue

                        if decoration == 0: break

                        selectedDecoration = decorationsDatabase[decoration-1]
                        if selectedDecoration['price'] > salesDatabase.balance:
                            os.system('clear||cls')
                            print(f'{TextStyle.RED}Insufficient Balance{TextStyle.END}')
                            input('\nPress Enter...')
                            continue
                        
                        while True:
                            try:
                                n = 0
                                locations: list[Location] = []

                                os.system('clear||cls')
                                for l in locationDatabase:
                                    locations.append(l)
                                    n += 1
                                    print(f'{n}. {l.name} ({l.description})')

                                locationId = int(input('\nChoose Location: '))
                                if 1 <= locationId <= n:
                                    break
                                else:
                                    os.system('clear||cls')
                                    print(f'{TextStyle.RED}Please Input A Number Between 1 - {n}{TextStyle.END}')
                                    input('\nPress Enter...')

                            except:
                                os.system('clear||cls')
                                print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                                input('\nPress Enter...')

                                
                        decorationDatabase.append(Decoration(selectedDecoration['name'], locationDatabase[locationId-1]._id))
                        
                        salesDatabase.sell(selectedDecoration['price'], f'Buy Decoration {selectedDecoration["name"]}')

                        os.system('clear||cls')
                        print(f'{TextStyle.GREEN}Decoration Added Successfully{TextStyle.END}')
                        input('\nPress Enter...')
                    except:
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                        input('\nPress Enter...')

        if choice == '2':
            while True:
                try:
                    os.system('clear||cls')
                    print('0. Exit')
                    for x, d in enumerate(decorationDatabase):
                        for l in locationDatabase:
                            if l._id == d.locationId:
                                print(f'{x+1}. {d.name} | {l.name}')

                    decoration = int(input('\nSelect Decoration: '))

                    if not(0 <= decoration <= len(decorationDatabase)):
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Please Input A Number Between 0 - {len(decorationsDatabase)}{TextStyle.END}')
                        input('\nPress Enter...')
                        continue

                    if decoration == 0: break
                    
                    while True:
                        try:
                            n = 0
                            locations: list[Location] = []

                            os.system('clear||cls')
                            for l in locationDatabase:
                                locations.append(l)
                                n += 1
                                print(f'{n}. {l.name} ({l.description})')

                            locationId = int(input('\nChoose Location: '))
                            if 1 <= locationId <= n:
                                break
                            else:
                                os.system('clear||cls')
                                print(f'{TextStyle.RED}Please Input A Number Between 1 - {n}{TextStyle.END}')
                                input('\nPress Enter...')
                        except:
                            os.system('clear||cls')
                            print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                            input('\nPress Enter...')

                    decorationDatabase[decoration-1].locationId = locationDatabase[locationId-1]._id

                    os.system('clear||cls')
                    print(f"{TextStyle.GREEN}Decoration Updated Successfully{TextStyle.END}")
                    input('\nPress Enter...')
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                    input('\nPress Enter...')

        if choice == '3':
            while True:
                try:
                    os.system('clear||cls')
                    print('0. Exit')
                    for x, d in enumerate(decorationDatabase):
                        for l in locationDatabase:
                            if l._id == d.locationId:
                                print(f'{x+1}. {d.name} | {l.name}')

                    decoration = int(input('\nSelect Decoration: '))

                    if not(0 <= decoration <= len(decorationDatabase)):
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Please Input A Number Between 0 - {len(decorationDatabase)}{TextStyle.END}')
                        input('\nPress Enter...')
                        continue

                    if decoration == 0: break

                    decorationDatabase.pop(decoration-1)

                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Decoration Deleted Successfuly{TextStyle.END}")
                    input('\nPress Enter...')
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                    input('\nPress Enter...')