from database import shop as shopDatabase
from database import location as locationDatabase
from database import product as productDatabase
import os
from models.Location import Location
from utilsFolder.text_style import TextStyle
from models.Shop import Shop

def shop():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Shop')
        print('2. Edit Shop')
        print('3. Delete Shop')

        choice = input('\nEnter Option: ')

        if choice == '0': break

        if choice == '1':
            # Check If Theres At Least 1 Location Available
            if len(locationDatabase) == 0: 
                os.system('clear||cls')
                print(f'{TextStyle.RED}No Locations Were Found, Please Create A New One...{TextStyle.END}')
                input('\nPress Enter...')
                break

            os.system('clear||cls')
            name = input('Name: ')

            productIds = []

            if len(productDatabase) == 0: 
                os.system('clear||cls')
                print(f'{TextStyle.RED}No Products Were Found, Please Create A New One...{TextStyle.END}')
                input('\nPress Enter...')
                break
            else:
                while True:
                    n = 1
                    productsNotStored = []

                    os.system('clear||cls')
                    for p in productDatabase:
                        if not (p._id in productIds):
                            productsNotStored.append(p)

                    # If All Products Have Been Stored Then Auto Complete This Section  
                    if len(productsNotStored) == 0:
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}All Products Have Been Stored, Proceed To The Next Section...{TextStyle.END}')
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
                        print(f'{TextStyle.RED}~ No Products Yet ~{TextStyle.END}')

                    prod = int(input('\nChoose Product: '))

                    if 0 <= prod <= n - 1:
                        if prod == 0: 
                            if len(productIds) == 0:
                                os.system('clear||cls')
                                print(f'{TextStyle.RED}Shop Must Contain At Least 1 Product{TextStyle.END}')
                                input('\nPress Enter...')
                                continue
                            break
                        productIds.append(productsNotStored[prod-1]._id)
                    else:
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Please Input A Number Between 0 - {n-1}{TextStyle.END}')
                        input('\nPress Enter...')
            
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

            shopDatabase.append(Shop(locationDatabase[locationId-1]._id, productIds, name))

            os.system('clear||cls')
            print(f'{TextStyle.GREEN}Shop Added Successfully{TextStyle.END}')
            input('\nPress Enter...')

        if choice == '2':
            try:
                while True:
                    # Check If Theres At Least 1 Shop
                    if len(shopDatabase) == 0: 
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}No Shops Were Found, Please Create A New One...{TextStyle.END}')
                        input('\nPress Enter...')
                        break
                    
                    while True:
                        try:
                            n = 1
                            os.system('clear||cls')
                            print('0. Exit')
                            for s in shopDatabase:
                                print(f'{n}. {s.name}')
                                n += 1
                            shop = int(input('\nChoose Shop: '))
                            break
                        except:
                            os.system('clear||cls')
                            print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                            input('\nPress Enter...')

                    if not(0 <= shop <= n-1): 
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Please Input A Number Between 0 - {n-1}{TextStyle.END}')
                        input('\nPress Enter...')
                        continue
                    if shop == 0: break

                    os.system('clear||cls')
                    name = input('Name: ')

                    productIds = shopDatabase[shop-1].productIds

                    if len(productDatabase) == 0: 
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}No Products Were Found, Please Create A New One...{TextStyle.END}")
                        input('\nPress Enter...')
                        break
                    else:
                        while True:
                            n = 1
                            productsNotStored = []
                            for p in productDatabase:
                                if not (p._id in productIds):
                                    productsNotStored.append(p)

                            # If All Products Have Been Stored Then Auto Complete This Section  
                            if len(productsNotStored) == 0:
                                os.system('clear||cls')
                                print(f"{TextStyle.RED}All Products Have Been Stored, Proceed To The Next Section...{TextStyle.END}")
                                input('\nPress Enter...')
                                break

                            os.system('clear||cls')
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
                                print(f"{TextStyle.RED}No Products Yet{TextStyle.END}")

                            prod = int(input('\nChoose Product: '))

                            if 0 <= prod <= n - 1:
                                if prod == 0: 
                                    if len(productIds) == 0:
                                        os.system('clear||cls')
                                        print(f"{TextStyle.RED}Shop Must Contain At Least 1 Product{TextStyle.END}")
                                        input('\nPress Enter...')
                                        continue
                                    break
                                productIds.append(productsNotStored[prod-1]._id)
                            else:
                                os.system('clear||cls')
                                print(f"{TextStyle.RED}Please Input A Number Between 0 - {n-1}{TextStyle.END}")
                                input('\nPress Enter...')

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

                    shopDatabase[shop-1] = Shop(locationDatabase[locationId-1]._id, productIds, name, shopDatabase[shop-1]._id)

                    os.system('clear||cls')
                    print(f'{TextStyle.GREEN}Shop Updated Successfully{TextStyle.END}')
                    input('\nPress Enter...')
            except:
                os.system('clear||cls')
                print(f'{TextStyle.RED}Input Must Be a Number{TextStyle.END}')
                input('\nPress Enter...')

        if choice == '3':
            while True:
                # Check If Theres At Least 1 Shop
                if len(shopDatabase) == 0: 
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}No Shop Were Found, Please Create A New One...{TextStyle.END}')
                    input('\nPress Enter...')
                    break

                n = 1

                os.system('clear||cls')
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
                            os.system('clear||cls')
                            print(f'{TextStyle.RED}Please Input A Number Between 0 - {n-1}{TextStyle.END}')
                            input('\nPress Enter...')
                        else:
                            break
                    except:
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                        input('\nPress Enter...')

                if shop == 0: break
                shopDatabase.pop(shop-1)

                os.system('clear||cls')
                print(f'{TextStyle.RED}Shop Deleted{TextStyle.END}')
                input('\nPress Enter...')