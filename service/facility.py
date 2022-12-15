from database import location as locationDatabase
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

            