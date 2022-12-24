from database import location as locationDatabase
from database import product as productDatabase
from database import facility as facilityDatabase
from models.Location import Location
from models.Facility import Facility
import os

def facility():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Facility')
        print('2. Edit Facility')
        print('3. Delete Facility')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            os.system('clear||cls')

            # Check If Theres At Least 1 Location Available
            if len(locationDatabase) == 0: 
                print('No Locations Were Found, Please Create A New One...')
                input('Press Enter...')
                break

            name = input('Name: ')

            hasProduct = 2

            while True:
                try:
                    os.system('clear||cls')
                    print('1. Yes')
                    print('2. No')
                    hasProduct = int(input('Has Product?: '))
                    if not (1 <= hasProduct <= 2):
                        print('Input A Number From 1 - 2')
                        input('Press Enter...')
                    else:
                        break
                except:
                    print('Please Input A Number')
                    input('Press Enter...')

            productIds = []

            if hasProduct == 1:
                # Check If Theres At Least 1 Product Available
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
                        print('\nProducts In This Facility: ')
                        for p in productIds:
                            for pd in productDatabase:
                                if p == pd._id:
                                    print(f'{pn}. {pd.name}')
                                    pn += 1

                        prod = int(input('Choose Product: '))

                        if 0 <= prod <= n - 1:
                            if prod == 0: break
                            productIds.append(productsNotStored[prod-1]._id)
                        else:
                            print(f'Please Input A Number Between 0 - {n-1}')
                            input('Press Enter...')

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
                except:
                    print('Please Input Number...')

            facilityDatabase.append(Facility(name, locations[locationId-1]._id, productIds))
            print('Product Added Successfully')
            input('Press Enter...')

        if choice == '2':
            os.system('clear||cls')

            # Check If Theres At Least 1 Facility
            if len(facilityDatabase) == 0: 
                print('No Facilities Were Found, Please Create A New One...')
                input('Press Enter...')
                break

            n = 1

            print('0. Exit')
            for f in facilityDatabase:
                print(f'{n}. {f.name} | ', end='')
                for l in locationDatabase:
                    if f.locationId == l._id:
                        print(l.name)
                n += 1

            while True:
                try:
                    facility = int(input('Choose Facility: '))
                    if not (0 <= facility <= n - 1):
                        print(f'Please Input A Number Between 0 - {n}')
                        input('Press Enter...')
                    else:
                        break
                except:
                    print("Input Must Be a Number")
            
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
                    hasProduct = int(input('Has Product?: '))
                    if not (1 <= hasProduct <= 2):
                        print('Input A Number From 1 - 2')
                        input('Press Enter...')
                    else:
                        break
                except:
                    print('Please Input A Number')
                    input('Press Enter...')

            productIds = []

            if hasProduct == 1:
                # Check If Theres At Least 1 Product Available
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
                        print('\nProducts In This Facility: ')
                        for p in productIds:
                            for pd in productDatabase:
                                if p == pd._id:
                                    print(f'{pn}. {pd.name}')
                                    pn += 1

                        prod = int(input('Choose Product: '))

                        if 0 <= prod <= n - 1:
                            if prod == 0: break
                            productIds.append(productsNotStored[prod-1]._id)
                        else:
                            print(f'Please Input A Number Between 0 - {n-1}')
                            input('Press Enter...')

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
                except:
                    print('Please Input Number...')

            facilityDatabase[facility-1] = Facility(name, locations[locationId-1]._id, productIds)
            print('Product Updated Successfully')
            input('Press Enter...')