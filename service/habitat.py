from models.Habitat import Habitat
import os
from database import animal as animalDatabase
from database import habitat as habitatDatabase
from database import location as locationDatabase
from models.Location import Location
from utilsFolder.text_style import TextStyle

def habitat():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Habitat')
        print('2. Edit Habitat')
        print('3. Delete Habitat')
        print('4. Show All Habitat By Location')

        choice = input('\nEnter Option: ')

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

            habitatDatabase.append(Habitat(locations[locationId-1]._id, name))

            os.system('clear||cls')
            print(f'{TextStyle.GREEN}Habitat Added Successfully{TextStyle.END}')
            input('\nPress Enter...')

        if choice == '4':
            while True:
                # Check If Theres At Least 1 Habitat
                if len(habitatDatabase) == 0:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}No Habitats Were Found{TextStyle.END}')
                    input('\nPress Enter...')
                    break
                else:
                    os.system('clear||cls')
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
                        input('\nPress Enter...')
                    except:
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Habitat Not Found{TextStyle.END}')
                        input('\nPress Enter...')

        if choice == '3':
            while True:
                # Check If Theres At Least 1 Habitat
                if len(habitatDatabase) == 0: 
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}No Habitats Were Found, Please Create A New One...{TextStyle.END}')
                    input('\nPress Enter...')
                    break

                while True:
                    try:
                        n = 1
                        os.system('clear||cls')
                        print('0. Exit')
                        for h in habitatDatabase:
                            print(f'{n}. {h.name}')
                            n += 1
                        habitat = int(input('\nChoose Habitat: '))
                        break
                    except:
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Input Must Be a Number{TextStyle.END}')
                        input('\nPress Enter...')

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
                        print(f'{TextStyle.RED}{totalAnimalFound} Animal(s) Found In This Habitat, Please Remove Them First{TextStyle.END}')
                        input('\nPress Enter...')
                    else:
                        habitatDatabase.pop(habitat-1)
                        os.system('clear||cls')
                        print(f'{TextStyle.GREEN}Habitat Deleted Successfuly{TextStyle.END}')
                        input('\nPress Enter...')
                except:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Please Input Number Between 0 - {n-1}{TextStyle.END}')
                    input('\nPress Enter...')

        if choice == '2':
            while True:
                # Check If Theres At Least 1 Habitat
                if len(habitatDatabase) == 0: 
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}No Habitats Were Found, Please Create A New One...{TextStyle.END}')
                    input('\nPress Enter...')
                    break

                while True:
                    try:
                        os.system('clear||cls')
                        print('0. Exit')
                        n = 1
                        for h in habitatDatabase:
                            print(f'{n}. {h.name}')
                            n += 1
                        habitat = int(input('\nChoose Habitat: '))
                        break
                    except:
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                        input('\nPress Enter...')

                try:
                    if not(0 <= habitat <= n-1): raise Exception
                    if habitat == 0: break

                    os.system('clear||cls')
                    name = input('Name: ')

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
                                print(f"{TextStyle.RED}Please Input A Number Between 1 - {n}{TextStyle.END}")
                                input('\nPress Enter...')
                        except:
                            os.system('clear||cls')
                            print(f"{TextStyle.RED}Please Input Number...{TextStyle.END}")
                            input('\nPress Enter...')
                
                    habitatDatabase[habitat-1] = Habitat(locations[locationId-1]._id, name, habitatDatabase[habitat-1]._id)

                    os.system('clear||cls')
                    print(f'{TextStyle.GREEN}Habitat Updated Successfully{TextStyle.END}')
                    input('\nPress Enter...')
                except:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Please Input Number Between 0 - {n-1}{TextStyle.END}')
                    input('\nPress Enter...')

                