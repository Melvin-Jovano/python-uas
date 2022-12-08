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
        print('4. Show All Habitat By Location')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            # Check If Theres At Least 1 Location Available
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
                        break
                    else:
                        print(f'Please Input A Number Between 1 - {n}')
                except:
                    print('Please Input Number...')

            habitatDatabase.append(Habitat(locations[locationId-1]._id, name))
            print('Habitat Added Successfully')
            input('Press Enter...')

        if choice == '4':
            while True:

                os.system('clear||cls')

                # Check If Theres At Least 1 Habitat
                if len(habitatDatabase) == 0:
                    print('No Habitat Were Found')
                    input('Press Enter...')
                    break
                else:
                    print('0. Exit')
                    locationThatHasHabitat = []

                    for h in habitatDatabase:
                        if h.locationId not in locationThatHasHabitat: 
                            locationThatHasHabitat.append(h.locationId)

                    habitatHashmap: dict[str, Habitat] = {}

                    locationNumber = 1
                    for l in locationDatabase:
                        if l._id in locationThatHasHabitat:
                            print(f'{locationNumber}. {l.name} - {l.description}')
                            habitatNumber = 1
                            
                            for h in habitatDatabase:
                                if h.locationId == l._id:
                                    number = f'{locationNumber}.{habitatNumber}'
                                    print(f'{number}. {h.name}')
                                    habitatHashmap[number] = h
                                    habitatNumber += 1
                        
                            print()
                            locationNumber += 1
                    
                    info = input('Select Habitat To Print Info: ')

                    if info == '0': break

                    try:
                        os.system('clear||cls')
                        habitatHashmap[info].printIntro()
                    except:
                        print('Habitat Not Found')
                input('Press Enter...')

    