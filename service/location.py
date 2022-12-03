from models.Location import Location
import os
from database import location as locationDatabase

def location():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Location')
        print('2. Edit Location')
        print('3. Delete Location')
        print('4. Show All Location')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            os.system('clear||cls')

            name = input('Location Name: ')
            description = input('Description: ')

            locationDatabase.append(Location(name, description))
            print('Location Added Successfully')
            input('Press Enter...')

        if choice == '4':
            for l in locationDatabase:
                print(f'ID: {l._id}, Name: {l.name}, Description: {l.description}')
            input('Press Enter...')

    