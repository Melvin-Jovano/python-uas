from models.Habitat import Habitat
import os
from database import animal as animalDatabase
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
            os.system('clear||cls')
            name = input('Habitat Name: ')

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

            habitatDatabase.append(Habitat(locations[locationId-1]._id, name))
            print('Habitat Added Successfully')
            input('Press Enter...')

        if choice == '4':
            while True:
                os.system('clear||cls')

                # Check If Theres At Least 1 Habitat
                if len(habitatDatabase) == 0:
                    print('No Habitats Were Found')
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

        if choice == '3':
            while True:
                os.system('clear||cls')

                # Check If Theres At Least 1 Habitat
                if len(habitatDatabase) == 0: 
                    print('No Habitats Were Found, Please Create A New One...')
                    input('Press Enter...')
                    break

                n = 1

                print('0. Exit')
                for h in habitatDatabase:
                    print(f'{n}. {h.name}')
                    n += 1

                while True:
                    try:
                        habitat = int(input('Choose Habitat: '))
                        break
                    except:
                        print("Input Must Be a Number")

                try:
                    if not(0 <= habitat <= n-1): raise Exception
                    if habitat == 0: break

                    totalAnimalFound = 0

                    # Check If Theres Animal In Selected Habitat
                    for a in animalDatabase:
                        if a.habitatId == habitatDatabase[habitat-1]._id:
                            totalAnimalFound += 1

                    if totalAnimalFound > 0:
                        os.system('clear||cls')
                        print(f'{totalAnimalFound} Animal(s) Found In This Habitat, Please Remove Them First')
                    else:
                        habitatDatabase.pop(habitat-1)
                        print('Habitat Deleted')

                    input('Press Enter...')
                except:
                    print(f'Please Input Number Between 0 - {n-1}')
                    input('Press Enter...')

        if choice == '2':
            while True:
                os.system('clear||cls')

                # Check If Theres At Least 1 Habitat
                if len(habitatDatabase) == 0: 
                    print('No Habitats Were Found, Please Create A New One...')
                    input('Press Enter...')
                    break

                n = 1

                print('0. Exit')
                for h in habitatDatabase:
                    print(f'{n}. {h.name}')
                    n += 1

                while True:
                    try:
                        habitat = int(input('Choose Habitat: '))
                        break
                    except:
                        print("Input Must Be a Number")

                try:
                    os.system('clear||cls')
                    if not(0 <= habitat <= n-1): raise Exception
                    if habitat == 0: break

                    name = input('Name: ')

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
                
                    habitatDatabase[habitat-1] = Habitat(locations[locationId-1]._id, name, habitatDatabase[habitat-1]._id)
                    print('Habitat Added Successfully')
                    input('Press Enter...')
                except:
                    print(f'Please Input Number Between 0 - {n-1}')
                    input('Press Enter...')

                