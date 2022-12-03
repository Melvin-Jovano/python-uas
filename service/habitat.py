from models.Habitat import Habitat
import os
from database import habitat as habitatDatabase
from database import location as locationDatabase

from models.Location import Location

def habitat():
    while True:
        os.system('clear||cls')
        
        print('0. Back')
        print('1. Add Habitat')
        print('2. Edit Habitat')
        print('3. Delete Habitat')
        print('4. Show All Habitat')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            # Check If Theres 1 Location Available
            if len(locationDatabase) == 0: 
                os.system('clear||cls')
                print('No Locations Were Found, Please Create A New One...')
                input('Press Enter...')
                break

            os.system('clear||cls')
            name = input('Habitat Name: ')

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
                        print(locations[locationId-1].name)
                        break
                    else:
                        print(f'Please Input A Number Between 1 - {n}')
                except:
                    print('Please Input Number...')
            

            habitatDatabase.append(Habitat(locationId, name))
            print('Habitat Added Successfully')
            input('Press Enter...')

        if choice == '4':
            for h in habitatDatabase:
                print(f'ID: {h._id}, Name: {h.name}')
            input('Press Enter...')

    