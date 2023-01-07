from database import location as locationDatabase
from database import product as productDatabase
from database import facility as facilityDatabase
from models.Location import Location
from models.Facility import Facility
from utilsFolder.text_style import TextStyle
import os

def facility():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Facility')
        print('2. Edit Facility')
        print('3. Delete Facility')

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

            hasProduct = 2

            while True:
                try:
                    os.system('clear||cls')
                    print('1. Yes')
                    print('2. No')
                    hasProduct = int(input('\nHas Product?: '))
                    if not (1 <= hasProduct <= 2):
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Input A Number From 1 - 2{TextStyle.END}')
                        input('\nPress Enter...')
                    else:
                        break
                except:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Please Input A Number{TextStyle.END}')
                    input('\nPress Enter...')

            productIds = []

            if hasProduct == 1:
                # Check If Theres At Least 1 Product Available
                if len(productDatabase) == 0: 
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}No Products Were Found, Please Create A New One...{TextStyle.END}')
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
                            print(f'{TextStyle.RED}All Products Have Been Stored, Proceed To The Next Section...{TextStyle.END}')
                            input('\nPress Enter...')
                            break

                        os.system('clear||cls')
                        print('0. Done')
                        for p in productsNotStored:
                            print(f'{n}. {p.name}, Stock: {p.stock}')
                            n += 1

                        pn = 1
                        hasProduct = False
                        print('\nProducts In This Facility: ')
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
                            if prod == 0: break
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

            facilityDatabase.append(Facility(name, locations[locationId-1]._id, productIds))

            os.system('clear||cls')
            print(f'{TextStyle.GREEN}Product Added Successfully{TextStyle.END}')
            input('\nPress Enter...')

        if choice == '2':
            # Check If Theres At Least 1 Facility
            if len(facilityDatabase) == 0: 
                os.system('clear||cls')
                print(f'{TextStyle.RED}No Facilities Were Found, Please Create A New One...{TextStyle.END}')
                input('\nPress Enter...')
                break

            n = 1

            os.system('clear||cls')
            print('0. Exit')
            for f in facilityDatabase:
                print(f'{n}. {f.name} | ', end='')
                for l in locationDatabase:
                    if f.locationId == l._id:
                        print(l.name)
                n += 1

            while True:
                try:
                    facility = int(input('\nChoose Facility: '))
                    if not (0 <= facility <= n - 1):
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Please Input A Number Between 0 - {n}{TextStyle.END}')
                        input('\nPress Enter...')
                    else:
                        break
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                    input('\nPress Enter...')
            
            if facility == 0:
                break

            os.system('clear||cls')
            name = input('Name: ')

            hasProduct = 2

            while True:
                try:
                    os.system('clear||cls')
                    print('1. Yes')
                    print('2. No')
                    hasProduct = int(input('\nHas Product?: '))
                    if not (1 <= hasProduct <= 2):
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Input A Number From 1 - 2{TextStyle.END}")
                        input('\nPress Enter...')
                    else:
                        break
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Please Input A Number{TextStyle.END}")
                    input('\nPress Enter...')

            productIds = []

            if hasProduct == 1:
                # Check If Theres At Least 1 Product Available
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
                        print('\nProducts In This Facility: ')
                        for p in productIds:
                            for pd in productDatabase:
                                if p == pd._id:
                                    print(f'{pn}. {pd.name}')
                                    pn += 1

                        prod = int(input('\nChoose Product: '))

                        if 0 <= prod <= n - 1:
                            if prod == 0: break
                            productIds.append(productsNotStored[prod-1]._id)
                        else:
                            os.system('clear||cls')
                            print(f'{TextStyle.RED}Please Input A Number Between 0 - {n-1}{TextStyle.END}')
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

            facilityDatabase[facility-1] = Facility(name, locations[locationId-1]._id, productIds)

            os.system('clear||cls')
            print(f'{TextStyle.GREEN}Product Updated Successfully{TextStyle.END}')
            input('\nPress Enter...')
        if choice == '3':
            while True:
                # Check If Theres At Least 1 Facility
                if len(facilityDatabase) == 0: 
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}No Facility Were Found, Please Create A New One...{TextStyle.GREEN}')
                    input('\nPress Enter...')
                    break


                while True:
                    try:
                        os.system('clear||cls')
                        print('0. Exit')
                        n = 1
                        for f in facilityDatabase:
                            print(f'{n}. {f.name} | ', end='')
                            for l in locationDatabase:
                                if f.locationId == l._id:
                                    print(l.name)
                                    n += 1
                        facility = int(input('\nChoose Facility: '))
                        if not(0 <= facility <= n-1): 
                            os.system('clear||cls')
                            print(f'{TextStyle.RED}Please Input A Number Between 0 - {n-1}{TextStyle.END}')
                            input('\nPress Enter...')
                        else:
                            break
                    except:
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                        input('\nPress Enter...')

                if facility == 0: break
                facilityDatabase.pop(facility-1)
                os.system('clear||cls')
                print(f'{TextStyle.GREEN}Facility Deleted{TextStyle.END}')
                input('\nPress Enter...')