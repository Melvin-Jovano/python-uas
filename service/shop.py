from database import shop as shopDatabase
from database import location as locationDatabase
from database import product as productDatabase
import os
from models.Location import Location

from models.Shop import Shop

def shop():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Shop')
        print('2. Edit Shop')
        print('3. Delete Shop')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            os.system('clear||cls')

            # Check If Theres At Least 1 Location Available
            if len(locationDatabase) == 0: 
                print('No Locations Were Found, Please Create A New One...')
                input('Press Enter...')
                break

            os.system('clear||cls')

            name = input('Name: ')

            productIds = []

            if len(productDatabase) == 0: 
                print('No Products Were Found, Please Create A New One...')
                input('Press Enter...')
                break
            else:
                while True:
                    os.system('clear||cls')
                    n = 1

                    productsNotStored = []

                    for p in productDatabase:
                        if not (p._id in productIds):
                            productsNotStored.append(p)

                    # If All Products Have Been Stored Then Auto Complete This Section  
                    if len(productsNotStored) == 0:
                        print('All Products Have Been Stored, Proceed To The Next Section...')
                        input('Press Enter...')
                        break

                    print('0. Done')
                    for p in productsNotStored:
                        print(f'{n}. {p.name}, Stock: {p.stock}')
                        n += 1

                    pn = 1
                    print('\nProducts In This Shop: ')
                    hasProduct = False
                    for p in productIds:
                        for pd in productDatabase:
                            if p == pd._id:
                                hasProduct = True
                                print(f'{pn}. {pd.name}')
                                pn += 1
                    if not hasProduct:
                        print('No Products Yet')

                    prod = int(input('\nChoose Product: '))

                    if 0 <= prod <= n - 1:
                        if prod == 0: 
                            if len(productIds) == 0:
                                print('Shop Must Contain At Least 1 Product')
                                input('\nPress Enter...')
                                continue
                            break
                        productIds.append(productsNotStored[prod-1]._id)
                    else:
                        print(f'Please Input A Number Between 0 - {n-1}')
                        input('\nPress Enter...')
            
            while True:
                try:
                    os.system('clear||cls')
                    n = 0
                    locations: list[Location] = []

                    for l in locationDatabase:
                        locations.append(l)
                        n += 1
                        print(f'{n}. {l.name} ({l.description})')

                    locationId = int(input('Choose Location: '))
                    if 1 <= locationId <= n:
                        break
                    else:
                        print(f'Please Input A Number Between 1 - {n}')
                        input('\nPress Enter...')
                except:
                    print('Please Input Number...')
                    input('\nPress Enter...')

            shopDatabase.append(Shop(locationDatabase[locationId-1]._id, productIds, name))
            print('Shop Added Successfully')
            input('\nPress Enter...')

        if choice == '2':
            while True:
                os.system('clear||cls')

                # Check If Theres At Least 1 Shop
                if len(shopDatabase) == 0: 
                    print('No Shops Were Found, Please Create A New One...')
                    input('\nPress Enter...')
                    break
                
                n = 1
                
                print('0. Exit')
                for s in shopDatabase:
                    print(f'{n}. {s.name}')
                    n += 1

                while True:
                    try:
                        shop = int(input('Choose Shop: '))
                        break
                    except:
                        print("Input Must Be a Number")
                        input('\nPress Enter...')

                os.system('clear||cls')
                if not(0 <= shop <= n-1): raise Exception
                if shop == 0: break

                name = input('Name: ')

                productIds = []

                if len(productDatabase) == 0: 
                    print('No Products Were Found, Please Create A New One...')
                    input('\nPress Enter...')
                    break
                else:
                    while True:
                        os.system('clear||cls')
                        n = 1

                        productsNotStored = []

                        for p in productDatabase:
                            if not (p._id in productIds):
                                productsNotStored.append(p)

                        # If All Products Have Been Stored Then Auto Complete This Section  
                        if len(productsNotStored) == 0:
                            print('All Products Have Been Stored, Proceed To The Next Section...')
                            input('\nPress Enter...')
                            break

                        print('0. Done')
                        for p in productsNotStored:
                            print(f'{n}. {p.name}, Stock: {p.stock}')
                            n += 1

                        pn = 1
                        print('\nProducts In This Shop: ')
                        hasProduct = False
                        for p in productIds:
                            for pd in productDatabase:
                                if p == pd._id:
                                    hasProduct = True
                                    print(f'{pn}. {pd.name}')
                                    pn += 1
                        if not hasProduct:
                            print('No Products Yet')

                        prod = int(input('\nChoose Product: '))

                        if 0 <= prod <= n - 1:
                            if prod == 0: 
                                if len(productIds) == 0:
                                    print('Shop Must Contain At Least 1 Product')
                                    input('\nPress Enter...')
                                    continue
                                break
                            productIds.append(productsNotStored[prod-1]._id)
                        else:
                            print(f'Please Input A Number Between 0 - {n-1}')
                            input('\nPress Enter...')

                os.system('clear||cls')
                while True:
                    try:
                        n = 0
                        locations: list[Location] = []

                        for l in locationDatabase:
                            locations.append(l)
                            n += 1
                            print(f'{n}. {l.name} ({l.description})')

                        locationId = int(input('Choose Location: '))
                        if 1 <= locationId <= n:
                            break
                        else:
                            print(f'Please Input A Number Between 1 - {n}')
                            input('\nPress Enter...')
                    except:
                        print('Please Input Number...')
                        input('\nPress Enter...')

                shopDatabase[shop-1] = Shop(locationDatabase[locationId-1]._id, productIds, name, shopDatabase[shop-1]._id)
                print('Shop Updated Successfully')
                input('\nPress Enter...')

        if choice == '3':
            while True:
                os.system('clear||cls')

                # Check If Theres At Least 1 Shop
                if len(shopDatabase) == 0: 
                    print('No Shop Were Found, Please Create A New One...')
                    input('Press Enter...')
                    break

                n = 1

                print('0. Exit')
                for f in shopDatabase:
                    print(f'{n}. {f.name} | ', end='')
                    for l in locationDatabase:
                        if f.locationId == l._id:
                            print(l.name)
                            n += 1

                while True:
                    try:
                        shop = int(input('Choose Shop: '))
                        if not(0 <= shop <= n-1): 
                            print(f'Please Input A Number Between 0 - {n-1}')
                            input('Press Enter...')
                        else:
                            break
                    except:
                        print("Input Must Be a Number")
                        input('Press Enter...')

                if shop == 0: break
                shopDatabase.pop(shop-1)
                print('Shop Deleted')
                input('Press Enter...')